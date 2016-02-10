
-- select * from auth_permission where codename like '%_employee';
-- select * from auth_permission where codename like '%_employeefamily';

-- select * from auth_permission where codename like '%_member';
-- select * from auth_permission where codename like '%_memberfamily';

-- select * from auth_permission where codename like '%_doctor';

-- select * from auth_permission where codename like '%_suppliercontact';


-- select * from django_content_type where app_label = 'employees' and model = 'employee';
-- select * from django_content_type where app_label = 'employees' and model = 'employeefamily';
-- select * from django_content_type where app_label = 'members' and model = 'member';
-- select * from django_content_type where app_label = 'members' and model = 'memberfamily';
-- select * from django_content_type where app_label = 'doctors' and model = 'doctor';
-- select * from django_content_type where app_label = 'suppliers' and model = 'suppliercontact';

/*********************************************************************************************/

update auth_permission set content_type_id = (select id from django_content_type where app_label = 'employees' and model = 'employee') where codename like '%_employee';
update auth_permission set content_type_id = (select id from django_content_type where app_label = 'employees' and model = 'employeefamily') where codename like '%_employeefamily';
update auth_permission set content_type_id = (select id from django_content_type where app_label = 'members' and model = 'member') where codename like '%_member';
update auth_permission set content_type_id = (select id from django_content_type where app_label = 'members' and model = 'memberfamily') where codename like '%_memberfamily';
update auth_permission set content_type_id = (select id from django_content_type where app_label = 'doctors' and model = 'doctor') where codename like '%_doctor';
update auth_permission set content_type_id = (select id from django_content_type where app_label = 'suppliers' and model = 'suppliercontact') where codename like '%_suppliercontact';
