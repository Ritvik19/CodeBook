SELECT comp.company_code,comp.founder,
    COUNT(DISTINCT(leadMgr.lead_manager_code)), COUNT(DISTINCT srMgr.senior_manager_code), 
    COUNT(DISTINCT mgr.manager_code), COUNT(DISTINCT emp.employee_code) 
FROM Employee emp, Manager mgr, Senior_Manager srMgr, Lead_Manager leadMgr , Company comp
WHERE emp.company_code = mgr.company_code 
    AND mgr.company_code = srMgr.company_code 
    AND srMgr.company_code = leadMgr.company_code 
    AND leadMgr.company_code = comp.company_code
GROUP BY comp.company_code , comp.founder ORDER BY comp.company_code;