# -*- coding: utf-8 -*-
from eea.facetednavigation.subtypes.interfaces import IPossibleFacetedNavigable
from plone import api
from plone.app.upgrade.utils import loadMigrationProfile
from zope.globalrequest import getRequest

import os


def reload_gs_profile(context):
    loadMigrationProfile(
        context,
        "profile-library.policy:default",
    )


# silly : default_language = fr
# root and folders are fr-be !
def change_language(context):
    pl = api.portal.get_tool("portal_languages")
    default_language = pl.getDefaultLanguage()
    root = api.portal.get()
    brains = api.content.find(root)
    for brain in brains:
        obj = brain.getObject()
        if obj.language != default_language:
            obj.language = default_language
    root.language = default_language


def configure_faceted(context):
    obj = api.portal.get()["explorer"]
    if not IPossibleFacetedNavigable.providedBy(obj):
        return
    subtyper = obj.restrictedTraverse("@@faceted_subtyper")

    if not subtyper:
        return
    subtyper.enable()
    faceted_config_path = "{}/faceted/config/explorer.xml".format(
        os.path.dirname(__file__)
    )
    with open(faceted_config_path, "rb") as faceted_config:
        obj.unrestrictedTraverse("@@faceted_exportimport").import_xml(
            import_file=faceted_config
        )
    request = getRequest()
