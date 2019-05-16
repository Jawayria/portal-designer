""" Theming / Site Branding Serializers"""
from rest_framework import serializers
from .models import SiteBranding
from wagtail.wagtailimages.models import Image


class ImageField(serializers.ReadOnlyField):
    """
    Field representing a Wagtail Image
    """

    def to_representation(self, value):
        """
        Returns a representation of a Wagtail image, specifically it returns the URL path.
        Args:
            value: (Image) wagtail image

        Returns:
            (str) url for image (does not include hostname)
        """
        return value.file.url


class OrganizationLogoField(serializers.ReadOnlyField):
    """
    Field representing an Organization Logo
    """

    def to_representation(self, value):
        """
        Returns a dict representing an Organization Logo
        Args:
            value: (SiteBranding) site branding object

        Returns:
            (dict) {
                    'url': (str) url for image (does not include hostname),
                    'alt': (str) alt text for image
                }
        """
        ret = {
            'url': value.organization_logo_image.file.url,
            'alt': value.organization_logo_alt_text,
        }
        return ret


class SiteBrandingSerializer(serializers.ModelSerializer):
    """
    Serializer for the SiteBranding model.
    """
    cover_image = ImageField()
    texture_image = ImageField()
    organization_logo = OrganizationLogoField(source='*')

    class Meta(object):
        model = SiteBranding
        read_only = True
        fields = (
            'program_title',
            'cover_image',
            'texture_image',
            'organization_logo',
            'banner_border_color',
        )