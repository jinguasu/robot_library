*** Settings ***
Library           nwi3_core.py
Library           nwi3_pm.py

*** Test Cases ***
1
    start_nwi3_core
    Vtk Verification For Many NEs    ${NE-OMS-list}
    stop_nwi3_core
