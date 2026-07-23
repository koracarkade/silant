from rest_framework import serializers

from machines.models import Machine
from maintenance.models import Maintenance
from complaints.models import Complaint



class MachineSerializer(serializers.ModelSerializer):

    machine_model = serializers.StringRelatedField()
    engine_model = serializers.StringRelatedField()
    transmission_model = serializers.StringRelatedField()
    drive_axle_model = serializers.StringRelatedField()
    steering_axle_model = serializers.StringRelatedField()

    client = serializers.StringRelatedField()
    service_company = serializers.StringRelatedField()


    class Meta:

        model = Machine

        fields = [
            "id",
            "factory_number",
            "machine_model",
            "engine_model",
            "engine_number",
            "transmission_model",
            "transmission_number",
            "drive_axle_model",
            "drive_axle_number",
            "steering_axle_model",
            "steering_axle_number",
            "shipment_date",
            "client",
            "service_company",
            "consignee",
            "delivery_address",
            "equipment",
        ]



class MaintenanceSerializer(serializers.ModelSerializer):

    machine = serializers.StringRelatedField()
    maintenance_type = serializers.StringRelatedField()


    class Meta:

        model = Maintenance

        fields = [
            "id",
            "machine",
            "maintenance_type",
            "maintenance_date",
            "description",
        ]



class ComplaintSerializer(serializers.ModelSerializer):

    machine = serializers.StringRelatedField()
    status = serializers.CharField(
        source="get_status_display"
    )


    class Meta:

        model = Complaint

        fields = [
            "id",
            "machine",
            "complaint_date",
            "description",
            "status",
        ]