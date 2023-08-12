"""
Main interface for quicksight service.

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_quicksight import (
        Client,
        ListAnalysesPaginator,
        ListAssetBundleExportJobsPaginator,
        ListAssetBundleImportJobsPaginator,
        ListDashboardVersionsPaginator,
        ListDashboardsPaginator,
        ListDataSetsPaginator,
        ListDataSourcesPaginator,
        ListGroupMembershipsPaginator,
        ListGroupsPaginator,
        ListIAMPolicyAssignmentsForUserPaginator,
        ListIAMPolicyAssignmentsPaginator,
        ListIngestionsPaginator,
        ListNamespacesPaginator,
        ListTemplateAliasesPaginator,
        ListTemplateVersionsPaginator,
        ListTemplatesPaginator,
        ListThemeVersionsPaginator,
        ListThemesPaginator,
        ListUserGroupsPaginator,
        ListUsersPaginator,
        QuickSightClient,
        SearchAnalysesPaginator,
        SearchDashboardsPaginator,
        SearchDataSetsPaginator,
        SearchDataSourcesPaginator,
        SearchGroupsPaginator,
    )

    session = Session()
    client: QuickSightClient = session.client("quicksight")

    list_analyses_paginator: ListAnalysesPaginator = client.get_paginator("list_analyses")
    list_asset_bundle_export_jobs_paginator: ListAssetBundleExportJobsPaginator = client.get_paginator("list_asset_bundle_export_jobs")
    list_asset_bundle_import_jobs_paginator: ListAssetBundleImportJobsPaginator = client.get_paginator("list_asset_bundle_import_jobs")
    list_dashboard_versions_paginator: ListDashboardVersionsPaginator = client.get_paginator("list_dashboard_versions")
    list_dashboards_paginator: ListDashboardsPaginator = client.get_paginator("list_dashboards")
    list_data_sets_paginator: ListDataSetsPaginator = client.get_paginator("list_data_sets")
    list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
    list_group_memberships_paginator: ListGroupMembershipsPaginator = client.get_paginator("list_group_memberships")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_iam_policy_assignments_paginator: ListIAMPolicyAssignmentsPaginator = client.get_paginator("list_iam_policy_assignments")
    list_iam_policy_assignments_for_user_paginator: ListIAMPolicyAssignmentsForUserPaginator = client.get_paginator("list_iam_policy_assignments_for_user")
    list_ingestions_paginator: ListIngestionsPaginator = client.get_paginator("list_ingestions")
    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_template_aliases_paginator: ListTemplateAliasesPaginator = client.get_paginator("list_template_aliases")
    list_template_versions_paginator: ListTemplateVersionsPaginator = client.get_paginator("list_template_versions")
    list_templates_paginator: ListTemplatesPaginator = client.get_paginator("list_templates")
    list_theme_versions_paginator: ListThemeVersionsPaginator = client.get_paginator("list_theme_versions")
    list_themes_paginator: ListThemesPaginator = client.get_paginator("list_themes")
    list_user_groups_paginator: ListUserGroupsPaginator = client.get_paginator("list_user_groups")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    search_analyses_paginator: SearchAnalysesPaginator = client.get_paginator("search_analyses")
    search_dashboards_paginator: SearchDashboardsPaginator = client.get_paginator("search_dashboards")
    search_data_sets_paginator: SearchDataSetsPaginator = client.get_paginator("search_data_sets")
    search_data_sources_paginator: SearchDataSourcesPaginator = client.get_paginator("search_data_sources")
    search_groups_paginator: SearchGroupsPaginator = client.get_paginator("search_groups")
    ```
"""
from .client import QuickSightClient
from .paginator import (
    ListAnalysesPaginator,
    ListAssetBundleExportJobsPaginator,
    ListAssetBundleImportJobsPaginator,
    ListDashboardsPaginator,
    ListDashboardVersionsPaginator,
    ListDataSetsPaginator,
    ListDataSourcesPaginator,
    ListGroupMembershipsPaginator,
    ListGroupsPaginator,
    ListIAMPolicyAssignmentsForUserPaginator,
    ListIAMPolicyAssignmentsPaginator,
    ListIngestionsPaginator,
    ListNamespacesPaginator,
    ListTemplateAliasesPaginator,
    ListTemplatesPaginator,
    ListTemplateVersionsPaginator,
    ListThemesPaginator,
    ListThemeVersionsPaginator,
    ListUserGroupsPaginator,
    ListUsersPaginator,
    SearchAnalysesPaginator,
    SearchDashboardsPaginator,
    SearchDataSetsPaginator,
    SearchDataSourcesPaginator,
    SearchGroupsPaginator,
)

Client = QuickSightClient

__all__ = (
    "Client",
    "ListAnalysesPaginator",
    "ListAssetBundleExportJobsPaginator",
    "ListAssetBundleImportJobsPaginator",
    "ListDashboardVersionsPaginator",
    "ListDashboardsPaginator",
    "ListDataSetsPaginator",
    "ListDataSourcesPaginator",
    "ListGroupMembershipsPaginator",
    "ListGroupsPaginator",
    "ListIAMPolicyAssignmentsForUserPaginator",
    "ListIAMPolicyAssignmentsPaginator",
    "ListIngestionsPaginator",
    "ListNamespacesPaginator",
    "ListTemplateAliasesPaginator",
    "ListTemplateVersionsPaginator",
    "ListTemplatesPaginator",
    "ListThemeVersionsPaginator",
    "ListThemesPaginator",
    "ListUserGroupsPaginator",
    "ListUsersPaginator",
    "QuickSightClient",
    "SearchAnalysesPaginator",
    "SearchDashboardsPaginator",
    "SearchDataSetsPaginator",
    "SearchDataSourcesPaginator",
    "SearchGroupsPaginator",
)
