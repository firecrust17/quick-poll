from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, MetaData
import datetime
from sqlalchemy import Integer, String, Time, Date, DateTime, DECIMAL, Unicode, Boolean
from sqlalchemy.dialects.postgresql import JSON
# from DCE.Leggero.Leggero_Model_Reflection import LeggeroApplicationDB
from sqlalchemy.orm import sessionmaker, relationship, deferred
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy.dialects.postgresql import JSONB
# from geoalchemy2 import Geometry
from decimal import Decimal
# Alias for datetime to update now_date as update hook.
from datetime import datetime as dt_alias
from sqlalchemy.types import ARRAY
# from DCE.service_handler.mosesexceptions import ColumnLengthMistmatch
# from DCE.commons.config_reader import LgConfig
# import pytz
from sqlalchemy import func

_ladb = LeggeroApplicationDB('DCEAPP')
_dbengine = _ladb.get_dbengine()

_mosesmetadata_in_use = _ladb.get_metadata('in_use')
_mosesmetadata_in_use.reflect(views=True)

decmetadata2 = MetaData(bind=_dbengine, schema='in_use')

Base = automap_base(metadata=_mosesmetadata_in_use)
DecBase = declarative_base(metadata=decmetadata2)

LC = LgConfig().getConfig()


class BizOrg(Base):
    __tablename__ = 'biz_org'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class Employee(Base):
    __tablename__ = 'employee'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lg_employee_case = relationship(
        "TableCase", back_populates="lg_case_employee")


class DivOrg(Base):
    __tablename__ = 'div_org'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class Site(Base):
    __tablename__ = 'site'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class SiteAddress(Base):
    __tablename__ = 'site_address'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class ClassificationValue(Base):
    __tablename__ = 'classification_value'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class ClassificationType(Base):
    __tablename__ = 'classification_type'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableUser(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())
    # lastchange_datetime = Column(DateTime, onupdate=dt_alias.now(), default=dt_alias.now())
    # create_datetime = Column(DateTime, default=dt_alias.now())


class TableUserProfile(Base):
    __tablename__ = 'user_profile'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class EmployeeDivOrg(Base):
    __tablename__ = 'employee_div_org'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())
    # lastchange_datetime = Column(DateTime, onupdate=dt_alias.now(), default=dt_alias.now())
    # create_datetime = Column(DateTime, default=dt_alias.now())


class TableUserUserProfile(Base):
    __tablename__ = 'user_user_profile'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class DivAddress(Base):
    __tablename__ = 'div_org_address'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableDivOrgSite(Base):
    __tablename__ = 'div_org_site'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class Address(Base):
    __tablename__ = 'address'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableWorkflow(Base):
    __tablename__ = 'workflow_obj'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lg_wf_case = relationship("TableCase", back_populates="lg_case_wf")
    lg_wf_wrkgrp = relationship(
        "TableWorkgroup", back_populates="lg_wrkgrp_wf")
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())
    # lastchange_datetime = Column(DateTime, onupdate=dt_alias.now(), default=dt_alias.now())
    # create_datetime = Column(DateTime, default=dt_alias.now())


class TableWorkgroup(Base):
    __tablename__ = 'workgroup'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lg_wrkgrp_wf = relationship('TableWorkflow', back_populates='lg_wf_wrkgrp', doc={
        "frontend_key": "workgroup2workflow"})
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())
    # lastchange_datetime = Column(DateTime, onupdate=dt_alias.now(), default=dt_alias.now())
    # create_datetime = Column(DateTime, default=dt_alias.now())


class TableUserWorkgroup(Base):
    __tablename__ = 'user_workgroup'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())
    # lastchange_datetime = Column(DateTime, onupdate=dt_alias.now(), default=dt_alias.now())
    # create_datetime = Column(DateTime, default=dt_alias.now())


class TableCase(Base):
    __tablename__ = 'case_table'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lg_case_wf = relationship("TableWorkflow", back_populates="lg_wf_case", doc={
        "frontend_key": "case2workflow"})
    lg_case_employee = relationship(
        "Employee", back_populates="lg_employee_case")
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())
    # lastchange_datetime = Column(DateTime, onupdate=dt_alias.now(), default=dt_alias.now())
    # create_datetime = Column(DateTime, default=dt_alias.now())


class TableCaseNotes(Base):
    __tablename__ = 'case_notes'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())


class TableRFQNotes(Base):
    __tablename__ = 'rfq_notes'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())


class TableQuoteNotes(Base):
    __tablename__ = 'quote_notes'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())


class TableOrderNotes(Base):
    __tablename__ = 'order_notes'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())


class TableTask(Base):
    __tablename__ = 'task'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class TableTaskNotes(Base):
    __tablename__ = 'task_notes'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())


class TableUserWorkgroupView(Base):
    __tablename__ = 'user_workgroups_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableBOQView(Base):
    __tablename__ = 'boq_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableDocuments(Base):
    __tablename__ = 'documents'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TablePriorityClassification(Base):
    __tablename__ = 'priority_classification'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableCaseView(Base):
    __tablename__ = 'case_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableTaskView(Base):
    __tablename__ = 'task_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableAdviceView(Base):
    __tablename__ = 'advice_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableAdviceReportView(Base):
    __tablename__ = 'advice_report_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableInternalEmployee(Base):
    __tablename__ = 'internal_employee'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class TableInternalEmployeeHeirarchy(Base):
    __tablename__ = 'internal_employee_heirarchy'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableInternalEmployeeDiv(Base):
    __tablename__ = 'internal_employee_div_org'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class UserWorkgroup(Base):
    __tablename__ = 'user_workgroup'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableSiteContactPerson(Base):
    __tablename__ = 'site_contact_person'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableContactPerson(Base):
    __tablename__ = 'contact_person'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableContactDetails(Base):
    __tablename__ = 'contact_details'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class SiteContactView(Base):
    __tablename__ = 'site_contact_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class AsiBusinessManagersView(Base):
    __tablename__ = 'asi_business_managers'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class BIReportManagerView(Base):
    __tablename__ = 'bi_report_manager_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class AsiAdminManagersView(Base):
    __tablename__ = 'asi_admin_managers'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class InternalEmployeeContactView(Base):
    __tablename__ = 'internal_employee_contact_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableWorkflowLog(Base):
    __tablename__ = 'workflow_log'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableInternalEmployeeSearchView(Base):
    __tablename__ = 'asi_employee_search_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableInternalEmployeeSearchViewWord(Base):
    __tablename__ = 'asi_employee_search_view_words'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableCertificates(Base):
    __tablename__ = 'certificates'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class AsiEmployeeView(Base):
    __tablename__ = 'asi_employee_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class AtAsiEmployeeDiv(Base):
    __tablename__ = 'at_asi_employee_div_org'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableEmployeeSearchView(Base):
    # View for searching the employee for a given employer(BizOrg), used for locating the emplloyee for tickets.
    __tablename__ = 'employee_search_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableEmployeeSearchViewWords(Base):
    # View for searching the employee for a given employer(BizOrg), used for locating the emplloyee for tickets.
    __tablename__ = 'employee_search_view_words'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableItemMaster(Base):
    __tablename__ = 'item_master'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class TableStockTransaction(Base):
    __tablename__ = 'stock_transaction'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())


class TableRFQ(Base):
    __tablename__ = 'rfq'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class TableBOQ(Base):
    __tablename__ = 'boq'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class TableQuote(Base):
    __tablename__ = 'quote'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class TableOrder(Base):
    __tablename__ = 'order'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class TableSiteContactUserView(Base):
    __tablename__ = 'site_contact_person_user_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableSiteContactPersonView(Base):
    __tablename__ = 'site_contact_person_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableRFQView(Base):
    __tablename__ = 'rfq_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableQuoteView(Base):
    __tablename__ = 'quote_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableTaskGroup(Base):
    __tablename__ = 'task_group'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class TableTaskGroupInstance(Base):
    __tablename__ = 'task_group_instance'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())


class TableUsersView(Base):
    __tablename__ = 'users_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableOrderView(Base):
    __tablename__ = 'order_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableNotificationDefination(Base):
    __tablename__ = 'notification_definition'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class TableNotiRFQView(Base):
    __tablename__ = 'noti_rfq_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableNotiQuoteView(Base):
    __tablename__ = 'noti_quote_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableNotiOrderView(Base):
    __tablename__ = 'noti_order_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableNotiTaskView(Base):
    __tablename__ = 'noti_task_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableNotiItemView(Base):
    __tablename__ = 'noti_item_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableNotiUserView(Base):
    __tablename__ = 'user_noti_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableNotiCertificatesView(Base):
    __tablename__ = 'noti_certificate_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableEmployeeProductsView(Base):
    __tablename__ = 'emp_products'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableNotiCaseView(Base):
    __tablename__ = 'noti_case_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableSequenceTracker(Base):
    __tablename__ = 'sequence_tracker'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableDispatchDefinition(Base):
    __tablename__ = 'dispatch_definition'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableDispatchRulesView(Base):
    __tablename__ = 'disptach_rules_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TablePriorityData(Base):
    __tablename__ = 'priority_data'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class TableWorkflowAction(Base):
    __tablename__ = 'workflow_action'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


class TableNotificationLog(Base):
    __tablename__ = 'notification_log'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())


class TableTaskGroupInstanceView(Base):
    __tablename__ = 'task_group_instance_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableEmailConfiguration(Base):
    __tablename__ = 'email_configuration'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())
    create_datetime = Column(DateTime, default=func.now())


# Roles Tables Mappers
# --------------##################-----------
# --------------##################-----------
# --------------##################-----------
# --------------##################-----------


class TableSidebar(Base):
    __tablename__ = 'sidebar'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableAssociationSidebar(Base):
    __tablename__ = 'association_sidebar'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableAssociationSidebarView(Base):
    __tablename__ = 'association_sidebar_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableComponent(Base):
    __tablename__ = 'component'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableComponentHeirarchy(Base):
    __tablename__ = 'component_heirarchy'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableComponentItems(Base):
    __tablename__ = 'component_items'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableAssociationComponentItems(Base):
    __tablename__ = 'association_component_items'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


# --------------##################-----------
# --------------##################-----------
# --------------##################-----------
# --------------##################-----------


class TableStockTransactionView(Base):
    __tablename__ = 'stock_transaction_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableEmployeeBizView(Base):
    __tablename__ = 'employee_biz_org_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableDBConfiguration(Base):
    __tablename__ = 'db_configuration'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableEmailConfigurationView(Base):
    __tablename__ = 'email_config_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


####################################Worfklow Log Views ##########################
#################################################################################
# Add workflow log view for RFQ, Quote, Order, Task here.

class TableCaseWfLogView(Base):
    __tablename__ = 'case_wf_log'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableAdviceWfLogView(Base):
    __tablename__ = 'advice_wf_log'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableTaskWfLogView(Base):
    __tablename__ = 'task_wf_log'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


#################################################################################
#################################################################################


###################################Audit Tables #################################


class TableAtCaseTable(Base):
    __tablename__ = 'at_case_table'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableAtAdvice(Base):
    __tablename__ = 'at_advice_table'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableAtTask(Base):
    __tablename__ = 'at_task'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


#################################################################################


###################################Notes Views Tables #################################

class TableCaseNotesView(Base):
    __tablename__ = 'case_notes_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableTaskNotesView(Base):
    __tablename__ = 'task_notes_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableAdviceNotesView(Base):
    __tablename__ = 'advice_notes_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


#################################################################################

class ProductHouse(Base):
    __tablename__ = 'product_house'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())


class Product(Base):
    __tablename__ = 'product'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class EmployeeProduct(Base):
    __tablename__ = 'employee_product'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class InboundFile(Base):
    __tablename__ = 'inbound_file'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())
    file_datetime = Column(DateTime, default=func.now())


#
# class EmployeeMedilife(Base):
#     __tablename__ = 'employee_medilife'
#     __table_args__ = {'extend_existing': 'True'}
#     id = Column(Integer, primary_key=True)
#

class EmployeeDiscovery(Base):
    __tablename__ = 'employee_discovery'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class BizOrgDivorgView(Base):
    __tablename__ = 'bizorg_divorg_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class ProductHouseView(Base):
    __tablename__ = 'product_house_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


#
# class EmployeeBestmed(Base):
#     __tablename__ = 'employee_bestmed'
#     __table_args__ = {'extend_existing': 'True'}
#     id = Column(Integer, primary_key=True)
#     lastchange_datetime = Column(
#         DateTime, onupdate=func.now(), default=func.now())
#     create_datetime = Column(DateTime, default=func.now())
#
#
class EmployeeBonitas(Base):
    __tablename__ = 'employee_bonitas'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class EmployeeBestmed(Base):
    __tablename__ = 'employee_bestmed'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


#
# class EmployeeCompcare(Base):
#     __tablename__ = 'employee_compcare'
#     __table_args__ = {'extend_existing': 'True'}
#     id = Column(Integer, primary_key=True)
#     lastchange_datetime = Column(
#         DateTime, onupdate=func.now(), default=func.now())
#     create_datetime = Column(DateTime, default=func.now())


class EmployeeFedhealth(Base):
    __tablename__ = 'employee_fedhealth'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)



class EmployeeHosmed(Base):
    __tablename__ = 'employee_hosmed'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class EmployeeMakoti(Base):
    __tablename__ = 'employee_makoti'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class EmployeeMedihelp(Base):
    __tablename__ = 'employee_medihelp'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


#
#
class EmployeeMedshield(Base):
    __tablename__ = 'employee_medishield'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)





class EmployeeMomentum(Base):
    __tablename__ = 'employee_momentum'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class EmployeeMotoHealth(Base):
    __tablename__ = 'employee_motohealth'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class EmployeeSizwe(Base):
    __tablename__ = 'employee_sizwe'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class EmployeeUmvuzo(Base):
    __tablename__ = 'employee_umvuzo'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TablePushNotification(Base):
    __tablename__ = 'push_notification'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())
    # create_datetime = Column(DateTime, default=dt_alias.now())


class BizOrgDivOrgEmployeeView(Base):
    __tablename__ = 'biorg_diorg_employee_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class DivSiteView(Base):
    __tablename__ = 'div_site_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableRFQQuoteWorkgroup(Base):
    __tablename__ = 'rfq_quote_wrkgrp'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableRFQQuoteWorkgroupView(Base):
    __tablename__ = 'quote_rfq_workgroup_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class HeirarchyView(Base):
    __tablename__ = 'heirarchy_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class UserProfileView(Base):
    __tablename__ = 'user_profile_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)










class ChronicConditions(Base):
    __tablename__ = 'chronic_conditions'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class BrokerSchemesData(Base):
    __tablename__ = 'schemes_data'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class GapData(Base):
    __tablename__ = 'gap_data'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TablePotentialMember(Base):
    __tablename__ = 'potential_member'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())


class TableAdvice(Base):
    __tablename__ = 'advice'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())


class TableAdviceNotes(Base):
    __tablename__ = 'advice_notes'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())


class TableInsuranceNeeds(Base):
    __tablename__ = 'insurance_needs'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())


class TableEmployeeDependents(Base):
    __tablename__ = 'employee_dependents'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())


class TablePotentialMemberDependents(Base):
    __tablename__ = 'potential_mem_dependents'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)
    create_datetime = Column(DateTime, default=func.now())
    lastchange_datetime = Column(
        DateTime, onupdate=func.now(), default=func.now())


class TableEmployeeDepView(Base):
    __tablename__ = 'employee_dependent_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TablePotentialDepView(Base):
    __tablename__ = 'pot_mem_dependent_view'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableSearchEmployeeFM(Base):
    __tablename__ = 'search_employee_view_for_fm'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableSearchEmployeeFNA(Base):
    __tablename__ = 'search_employee_view_for_fna'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableSearchEmployeeFNAWords(Base):
    __tablename__ = 'employee_search_view_words_fna'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


class TableTooltipItems(Base):
    __tablename__ = 'tooltip_items'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)






Base.prepare()

table_name_to_class_names = {
    'employee_discovery': EmployeeDiscovery,
    'employee_bestmed': EmployeeBestmed,
    'employee_bonitas': EmployeeBonitas,
    'employee_fedhealth': EmployeeFedhealth,
    'employee_medihelp': EmployeeMedihelp,
    'employee_medshield': EmployeeMedshield,
    'employee_sizwe': EmployeeSizwe,
    'employee_umvuzo': EmployeeUmvuzo
}

db_model_map = {
    item[0]: item[1] for item in Base._decl_class_registry.items()
}

breadcrumb_table_map = {'0514': 'ProductHouse', '09a9': 'TableTaskGroupInstance',
                        '0acc': 'BizOrg', '0d4b': 'Product', '0e4f': 'TableInternalEmployeeHeirarchy',
                        '1053': 'Site', '10fc': 'TableSiteContactPerson', '1153': 'EmployeeDivOrg',
                        '11ff': 'TableRFQ', '1302': 'DivOrg',
                        '4984': 'Address', '4dcc': 'Employee', '4e19': 'TableTaskGroup',
                        '5e48': 'TableNotificationDefination',
                        '68d5': 'TableDispatchDefinition', '6944': 'TableTask', '6f81': 'TableContactPerson',
                        '6fb9': 'TableDivOrgSite', '7008': 'TableInternalEmployee',
                        '7623': 'TableOrderNotes',
                        '8341': 'UserWorkgroup', '91c2': 'DivAddress',
                        'a098': 'TableUserWorkgroup', 'a27d': 'ClassificationType',
                        'd7ef': 'TableItemMaster',
                        'db38': 'TableCase'}


def orm_to_dict(obj):
    return {col.name: getattr(obj, col.name) for col in obj.__table__.columns}


def orm_to_dict_v2(obj, date_format=None):
    data = {}
    for col in obj.__table__.columns:
        if isinstance(getattr(obj, col.name), datetime.date):
            if date_format:
                data[col.name] = getattr(obj, col.name).strftime(date_format)
            else:
                data[col.name] = str(getattr(obj, col.name))
        elif isinstance(getattr(obj, col.name), datetime.time):
            data[col.name] = str(getattr(obj, col.name))
        elif isinstance(getattr(obj, col.name), Decimal):
            data[col.name] = round(float(getattr(obj, col.name)))
        else:
            data[col.name] = getattr(obj, col.name)
    return data


def orm_to_dict_selected(data, table_cols, date_format=None):
    datalist = []
    for _rec in data:
        data = {}
        for _val in zip(_rec, table_cols):
            dtype = _val[1].type.python_type
            if dtype == datetime.datetime:
                if date_format:
                    data_val = _val[0].strftime(date_format)
                else:
                    data_val = str(_val[0])
            elif dtype == datetime.date:
                data_val = str(_val[0])
            elif dtype == datetime.time:
                data_val = str(_val[0])
            elif dtype == Decimal:
                data_val = round(float(_val[0]))
            else:
                data_val = _val[0]
            data.update({_val[1].name: data_val})
        datalist.append(data)
    return datalist


def orm_to_dict_selected_with_col_aliases(data, table_cols, alias_cols=[], date_format=None):
    if len(table_cols) != len(alias_cols):
        raise ColumnLengthMistmatch
    datalist = []
    for _rec in data:
        data = {}
        for _val in zip(_rec, table_cols, alias_cols):
            dtype = _val[1].type.python_type
            if dtype == datetime.datetime:
                if date_format:
                    data_val = _val[0].strftime(date_format)
                else:
                    data_val = str(_val[0])
            elif dtype == datetime.date:
                data_val = str(_val[0])
            elif dtype == datetime.time:
                data_val = str(_val[0])
            elif dtype == Decimal:
                data_val = round(float(_val[0]))
            else:
                data_val = _val[0]
            data.update({_val[2]: data_val})
        datalist.append(data)
    return datalist


if __name__ == "__main__":
    pass
