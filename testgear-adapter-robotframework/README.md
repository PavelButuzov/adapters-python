# Test Gear TMS adapter for Robot Framework
![Test Gear](https://raw.githubusercontent.com/testgear-tms/adapters-python/master/images/banner.png)

## Getting Started

### Compatibility

| Test Gear | Adapter |
|-----------|---------|
| 3.5       | 2.0     |
| 4.0       | 2.1     |

### Installation
```
pip install testgear-adapter-robotframework
```

## Usage

### Configuration

#### File

1. Create **connection_config.ini** file in the root directory of the project:
    ```
    [testgear]
    URL = <url>
    privateToken = <token>
    projectId = <id>
    configurationId = <id>
    testRunId = <optional id>
    testRunName = <optional name>
    adapterMode = <optional>
    certValidation = <optional boolean>
    
    # This section are optional. It enables debug mode.
    [debug]
    tmsProxy = {"http": "http://localhost:8888", "https": "http://localhost:8888"}
    ```

2. Fill parameters with your configuration, where:  
    * `URL` - location of the TMS instance  
      
    * `privateToken` - API secret key
        1. go to the https://{DOMAIN}/user-profile profile
        2. copy the API secret key
    
    * `projectId` - ID of project in TMS instance.
    
        1. create a project
        2. open DevTools -> network
        3. go to the project https://{DOMAIN}/projects/{PROJECT_GLOBAL_ID}/tests
        4. GET-request project, Preview tab, copy id field  
    
    * `configurationId` - ID of configuration in TMS instance.
    
        1. create a project  
        2. open DevTools -> network  
        3. go to the project https://{DOMAIN}/projects/{PROJECT_GLOBAL_ID}/tests  
        4. GET-request configurations, Preview tab, copy id field  
    
    * `testRunId` - id of the created test run in TMS instance. `testRunId` is optional. If it is not provided, it is created automatically.  
      
    * `testRunName` - parameter for specifying the name of test run in TMS instance. `testRunName` is optional. If it is not provided, it is created automatically.   
    
    * `adapterMode` - adapter mode. Default value - 0. The adapter supports following modes:  
        
        * 0 - in this mode, the adapter filters tests by test run ID and configuration ID, and sends the results to the test run.
        * 1 - in this mode, the adapter sends all results to the test run without filtering.
        * 2 - in this mode, the adapter creates a new test run and sends results to the new test run.
   
    * `certValidation` - it enables/disables certificate validation. `certValidation` is optional.
    
    * `tmsProxy` - it enables debug mode. `tmsProxy` is optional.
    
3. Import `TMSLibrary` in your RobotFramework Tests (see `examples` directory)

#### ENV

You can use environment variables (environment variables take precedence over file variables):

* `TMS_URL` - location of the TMS instance.
  
* `TMS_PRIVATE_TOKEN` - API secret key.
  
* `TMS_PROJECT_ID` - ID of a project in TMS instance.
  
* `TMS_CONFIGURATION_ID` - ID of a configuration in TMS instance.

* `TMS_ADAPTER_MODE` - adapter mode. Default value - 0.
  
* `TMS_TEST_RUN_ID` - ID of the created test-run in TMS instance. `TMS_TEST_RUN_ID` is optional. If it is not provided, it is created automatically.
  
* `TMS_TEST_RUN_NAME` - name of the new test-run.`TMS_TEST_RUN_NAME` is optional. If it is not provided, it is created automatically.
  
* `TMS_CONFIG_FILE` - name of the configuration file. `TMS_CONFIG_FILE` is optional. If it is not provided, it is used default file name.

* `TMS_PROXY` - it enables debug mode. `TMS_PROXY` is optional.

* `TMS_CERT_VALIDATION` - it enables/disables certificate validation. `TMS_CERT_VALIDATION` is optional.

#### Command line

You also can use CLI variables, that sent to Robot Framework via `-v` option  (CLI variables take precedence over environment variables):

* `tmsUrl` - location of the TMS instance.
  
* `tmsPrivateToken` - API secret key.
  
* `tmsProjectId` - ID of a project in TMS instance.
  
* `tmsConfigurationId` - ID of a configuration in TMS instance.

* `tmsAdapterMode` - adapter mode. Default value - 0.

* `tmsTestRunId` - ID of the created test-run in TMS instance. `tmsTestRunId` is optional. If it is not provided, it is created automatically.
  
* `tmsTestRunName` - name of the new test-run.`tmsTestRunName` is optional. If it is not provided, it is created automatically.
  
* `tmsConfigFile` - name of the configuration file. `tmsConfigFile` is optional. If it is not provided, it is used default file name.

* `tmsProxy` - it enables debug mode. `tmsProxy` is optional.

* `tmsCertValidation` - it enables/disables certificate validation. `tmsCertValidation` is optional.

#### Examples

Launch with a connection_config.ini file in the root directory of the project:

```
$ robot -v testgear <test directory>
```

Launch with command-line parameters (parameters are case-insensitive):

```
$ robot -v testgear -v tmsUrl:<url> -v tmsPrivateToken:<token> -v tmsProjectId:<id> -v tmsConfigurationId:<id> -v tmsTestRunId:<optional id> -v tmsTestRunName:<optional name> -v tmsProxy:'{"http":"http://localhost:8888","https":"http://localhost:8888"}' -v tmsConfigFile:<optional file> -v tmsCertValidation:<optional boolean> <test directory>
```

If you want to enable debug mode then see [How to enable debug logging?](https://github.com/testgear-tms/adapters-python/tree/main/testgear-python-commons)

### Tags

Tags can be used to specify information about autotest. Tags are space sensitive, use only one space between words.

Description of tags:
- `testgear.workItemsId` - linking an autotest to a test case
- `testgear.displayName` - name of the autotest in the TMS system (default - name of test)
- `testgear.externalId` - ID of the autotest within the project in the TMS System
- `testgear.title` - title in the autotest card (default - name of test)
- `testgear.description` - description in the autotest card (default - documentation of test)
- `testgear.links` - links in the autotest card
- `testgear.labels` - labels in the autotest card

Description of methods:
- `Add Links` - links in the autotest result
- `Add Link` - add one link in the autotest result
- `Add Attachments` - uploading files in the autotest result
- `Add Attachment` - upload given content with given filename in the autotest result
- `Add Message` - information about autotest in the autotest result

### Parallel execution

You can also run your test in parallel with [Pabot](https://pabot.org/).

```
$ pabot --pabotlib -v testgear <test directory>
```

All other settings are the same as for standard execution.

### Examples

```robotframework
*** Settings ***
Documentation      Main Suite with examples
Library            testgear_adapter_robotframework.TMSLibrary

*** Variables ***
&{SIMPLE_LINK}             url=http://google.com
&{FULL_LINK}               url=http://google.co.uk   title=Google     type=Related   description=just a link

@{LINKS}               ${SIMPLE_LINK}   ${FULL_LINK}


*** Test Cases ***
Simple Test
    [Setup]  Setup
    Do Something
    Do Another Thing
    Log  I'am a step
    [Teardown]  Teardown

Simple Test with link as variable
    [Tags]   testgear.links:${SIMPLE_LINK}
    [Setup]  Setup
    Do Something
    Do Another Thing
    Log  I'am a step
    [Teardown]  Teardown

Simple Test with link as dict
    [Tags]   testgear.links:${{{'url': 'http://google.com', 'type':'Issue'}}}
    [Setup]  Setup
    Do Something
    Do Another Thing
    Log  I'am a step
    [Teardown]  Teardown

Simple Test with WorkitemId as string
    [Tags]   testgear.workitemsID:123
    [Setup]  Setup
    Do Something
    Do Another Thing
    Log  I'am a step
    [Teardown]  Teardown

Simple Test with WorkitemId as list
    [Tags]   testgear.workitemsID:${{[123, '456']}}
    [Setup]  Setup
    Do Something
    Do Another Thing
    Log  I'am a step
    [Teardown]  Teardown

Simple Test with Title or Description or DisplayName with simple formatting
    [Documentation]  Tags are space sensitive, use only one space between words
    [Tags]   testgear.displayName:This works     testgear.title:'This also works'
    ...    testgear.description:"This works too"
    [Setup]  Setup
    Do Something
    Do Another Thing
    Log  I'am a step
    [Teardown]  Teardown

Test With All Params
    [Documentation]  It's better to use this kind of formatting for different data types in tags
    [Tags]   testgear.externalID:123    testgear.title:${{'Different title'}}   testgear.displayName:${{'Different name'}}
    ...     testgear.description:${{'Different description'}}    testgear.workitemsID:${{[123, '456']}}
    ...     testgear.links:${{{'url': 'http://google.com', 'type':'Issue'}}}   testgear.labels:${{['smoke', 'lol']}}
    [Setup]  Setup
    Log    Something
    Log    Another
    [Teardown]  Teardown

Test With Add Link
    [Setup]  Setup
    Do Something
    Do Another Thing
    Add Links    @{LINKS}
#    You can also add one link (default type is Defect)
    Add Link    http://ya.ru
    Add Link    http://ya.ru    type=Issue
    Add Link    ${SIMPLE_LINK}[url]
    [Teardown]  Teardown

Test With Add Attachment
    [Setup]  Setup
    Do Something
    Do Another Thing
    ${V}   Get Variables
    Add Attachment    '${V}'    file.txt
    Add Attachments    images/banner.png     images/icon.png
    [Teardown]  Teardown

Test With Add Message
    [Setup]  Setup
    Do Something
    Do Another Thing
    Add Message    Wow, it's my error message!
    Fail
    [Teardown]  Teardown
```

# Contributing

You can help to develop the project. Any contributions are **greatly appreciated**.

* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/testgear-tms/adapters-python/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/testgear-tms/adapters-python/blob/master/CODE_OF_CONDUCT.md) before posting your first idea as well.

# License

Distributed under the Apache-2.0 License. See [LICENSE](https://github.com/testgear-tms/adapters-python/blob/master/LICENSE.md) for more information.

