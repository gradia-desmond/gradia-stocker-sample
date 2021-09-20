import os
from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.utils.timezone import utc
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Parcel, Receipt, ParcelTransfer, BasicGradingMixin
from .forms import SarineUploadForm, BasicUploadForm

from stonegrading.mixins import SarineGradingMixin

from .forms import CSVImportForm


class ReturnToVaultView(View):
    def get(self, request, pk, *args, **kwargs):
        parcel = Parcel.objects.get(pk=pk)
        try:
            ParcelTransfer.can_create_transfer(
                item=parcel, from_user=request.user, to_user=User.objects.get(username="vault")
            )
        except Exception as e:
            return HttpResponse(e)

        return render(
            request, "grading/return_to_vault_confirmation.html", {"username": request.user.username, "item": parcel}
        )

    def post(self, request, pk, *args, **kwargs):
        parcel = Parcel.objects.get(pk=pk)
        try:
            ParcelTransfer.can_create_transfer(
                item=parcel, from_user=request.user, to_user=User.objects.get(username="vault")
            )
        except Exception as e:
            return HttpResponse(e)
        ParcelTransfer.initiate_transfer(
            item=parcel, from_user=request.user, to_user=User.objects.get(username="vault"), created_by=request.user
        )
        return HttpResponseRedirect(reverse("admin:grading_parcel_change", args=[parcel.id]))


class ConfirmReceivedView(View):
    def get(self, request, pk, *args, **kwargs):
        parcel = Parcel.objects.get(pk=pk)

        try:
            ParcelTransfer.can_confirm_received(parcel, request.user)
        except Exception as e:
            return HttpResponse(e)

        parcel_owner, status = parcel.current_location()

        return render(request, "grading/confirm_received.html", {"username": request.user.username, "item": parcel})

    def post(self, request, pk, *args, **kwargs):
        parcel = Parcel.objects.get(pk=pk)
        try:
            ParcelTransfer.can_confirm_received(parcel, request.user)
        except Exception as e:
            return HttpResponse(e)

        ParcelTransfer.confirm_received(parcel)
        return HttpResponseRedirect(reverse("admin:grading_parcel_change", args=[parcel.id]))


class CloseReceiptView(View):
    def get(self, request, pk, *args, **kwargs):
        receipt = Receipt.objects.get(pk=pk)
        return render(request, "grading/close_receipt.html", {"username": request.user.username, "receipt": receipt})

    def post(self, request, pk, *args, **kwargs):
        receipt = Receipt.objects.get(pk=pk)
        receipt.release_by = request.user
        receipt.release_date = datetime.utcnow().replace(tzinfo=utc)
        receipt.save()
        return HttpResponseRedirect(reverse("admin:grading_receipt_change", args=[receipt.id]))


# @ConradHo ---> Possible refactor here, to help make error messages better (improving user experience)
def clean_basic_csv_upload_file(file_path):
    """
    Validate the file by checking the column field names if they're valid, validating the content of the
    field values and return a tuple of True and the field values, else return False and None
    :param file_path:
    :return:
    """
    pass


class AllUploadView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        template = "grading/all-uploads-to.html"
        context = {}
        return render(request, template, context)


class SarineUploadView(LoginRequiredMixin, View):
    fields = [field.name for field in SarineGradingMixin._meta.get_fields()] + ["internal_id"]

    def get(self, request, *args, **kwargs):
        """
        Page to return the HTML for sarine data upload
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = CSVImportForm()
        context = {"template_title": "Upload a csv file containing sarine data", "form": form}
        return render(request, "grading/upload.html", context)

    def post(self, request, *args, **kwargs):
        """
        Get csv file content with pandas
        Convert pandas data to dictionary
        loop through diction to create Stone instances while performing other operations such:
        - Ownership transfer stuff,
        - etc
        Split parcel (csv file) into stones by creating stone instances, etc
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = SarineUploadForm(user=request.user, data={}, files=request.FILES)
        if not form.is_valid():
            # get the csv errors and return them to some template as context variables and render as error page
            HttpResponseRedirect(reverse("grading:sarine_data_upload_url"))
        stones = form.save()
        split_id = stones[0].split_from.pk

        return HttpResponseRedirect(reverse("admin:grading_split_change", args=(split_id,)))


class BasicGradingUploadView(LoginRequiredMixin, View):
    fields = [field.name for field in BasicGradingMixin._meta.get_fields()]
    fields.append("internal_id")

    def get(self, request, *args, **kwargs):
        """
        Page to return HTML for upload input field
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        context = {"template_title": "Upload a csv file containing basic grading data"}
        if "errors" in kwargs:
            context["errors"] = kwargs["errors"]
        return render(request, "grading/upload.html", context)

    # def _process_graders(self, data_dict):
    #     """
    #     Return the basic graders or None. Eg. {"basic_grader_1"}
    #     """
    #     # Will change this implementation later for a better way of giving error messages
    #     graders = {"basic_grader_1": None, "basic_grader_2": None, "basic_grader_3": None}
    #
    #     for grader in graders:
    #         try:
    #             graders[grader] = User.objects.get(username=data_dict[grader])
    #         except User.DoesNotExist:
    #             pass
    #
    #     return graders

    # Simple table for displaying the errors == form.errors = {"height": []}

    def post(self, request, *args, **kwargs):
        """
        Decouple file and do the splitting
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = BasicUploadForm(data={}, files=request.FILES)
        if not form.is_valid():
            HttpResponseRedirect(reverse("grading:sarine_data_upload_url"))

        form.save()
        return HttpResponseRedirect(reverse("grading:basic_grading_data_upload_url"))


"""
class ConfirmTransferToGoldwayView(View):
    def get(self, request, pk, *args, **kwargs):
        stone = Stone.objects.get(pk=pk)
        assert stone.goldway_verification == ""
        return render(request, "grading/confirm_received.html", {"username": request.user.username, "item": parcel})

    def post(self, request, pk, *args, **kwargs):
        parcel = Parcel.objects.get(pk=pk)
        try:
            ParcelTransfer.can_confirm_received(parcel, request.user)
        except Exception as e:
            return HttpResponse(e)

        ParcelTransfer.confirm_received(parcel)
        return HttpResponseRedirect(reverse("admin:grading_parcel_change", args=[parcel.id]))
"""
