*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixture
Suite Teardown  Run Keyword And Ignore Error  Destroy Fixture

*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  firstname1  middlename1  lastname1  nickname1  title1  company1   address1  home1  11111111   1111111  111111  test@te.te    test@te.te     test@te.te    11111.1111  111111   11111111  111111  1  January   1991  1  January  2001
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}



Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Edit contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Edit Contact  ${contact}
    ${new_contact}=  Edited Contact  firstname1  middlename1  lastname1  nickname1  title1  company1   address1  home1  11111111   1111111  111111  test@te.te    test@te.te     test@te.te    11111.1111  111111   11111111  111111  1  January   1991  1  January  2001
    Update Contact  ${new_contact}
    ${new_list}=  Get Contact List
    ${old_list}=  Update Old List  ${old_list}  ${new_contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}