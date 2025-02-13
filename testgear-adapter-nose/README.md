# Test Gear TMS adapter for Nose

![Test Gear](https://raw.githubusercontent.com/testgear-tms/adapters-python/master/images/banner.png)

## Getting Started

### Compatibility

| Test Gear | Adapter |
|-----------|---------|
| 3.5       | 2.0     |
| 4.0       | 2.1     |

### Installation

```
pip install testgear-adapter-nose
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

    * `testRunId` - id of the created test run in TMS instance. `testRunId` is optional. If it is not provided, it is
      created automatically.

    * `testRunName` - parameter for specifying the name of test run in TMS instance. `testRunName` is optional. If it is
      not provided, it is created automatically.

    * `adapterMode` - adapter mode. Default value - 0. The adapter supports following modes:

        * 0 - in this mode, the adapter filters tests by test run ID and configuration ID, and sends the results to the
          test run.
        * 1 - in this mode, the adapter sends all results to the test run without filtering.
        * 2 - in this mode, the adapter creates a new test run and sends results to the new test run.
    
    * `certValidation` - it enables/disables certificate validation. `certValidation` is optional.

    * `tmsProxy` - it enables debug mode. `tmsProxy` is optional.

3. Create **unittest.cfg** file in the root directory of the project:
   ```
    [unittest]
    plugins = testgear_adapter_nose.plugin
    ```

#### ENV

You can use environment variables (environment variables take precedence over file variables):

* `TMS_URL` - location of the TMS instance.

* `TMS_PRIVATE_TOKEN` - API secret key.

* `TMS_PROJECT_ID` - ID of a project in TMS instance.

* `TMS_CONFIGURATION_ID` - ID of a configuration in TMS instance.

* `TMS_ADAPTER_MODE` - adapter mode. Default value - 0.

* `TMS_TEST_RUN_ID` - ID of the created test-run in TMS instance. `TMS_TEST_RUN_ID` is optional. If it is not provided,
  it is created automatically.

* `TMS_TEST_RUN_NAME` - name of the new test-run.`TMS_TEST_RUN_NAME` is optional. If it is not provided, it is created
  automatically.

* `TMS_CONFIG_FILE` - name of the configuration file. `TMS_CONFIG_FILE` is optional. If it is not provided, it is used
  default file name.

* `TMS_PROXY` - it enables debug mode. `TMS_PROXY` is optional.

* `TMS_CERT_VALIDATION` - it enables/disables certificate validation. `TMS_CERT_VALIDATION` is optional.

#### Examples

Launch with a connection_config.ini file in the root directory of the project:

```
$ nose2 --testgear
```

If you want to enable debug mode then
see [How to enable debug logging?](https://github.com/testgear-tms/adapters-python/tree/main/testgear-python-commons)

### Decorators

Decorators can be used to specify information about autotest.

Description of decorators:

- `testgear.workItemIds` - linking an autotest to a test case
- `testgear.displayName` - name of the autotest in the TMS system (can be replaced with documentation strings)
- `testgear.externalId` - ID of the autotest within the project in the TMS System
- `testgear.title` - title in the autotest card
- `testgear.description` - description in the autotest card
- `testgear.labels` - tags in the work item
- `testgear.link` - links in the autotest card
- `testgear.step` - the designation of the step called in the body of the test or other step

All decorators support the use of parameterization attributes

Description of methods:

- `testgear.addLinks` - links in the autotest result
- `testgear.addAttachments` - uploading files in the autotest result
- `testgear.addMessage` - information about autotest in the autotest result
- `testgear.step` - usage in the "with" construct to designation a step in the body of the test

### Examples

#### Simple test

```py
import pytest
import testgear


# Test with a minimal set of decorators
@testgear.externalId('Simple_autotest2')
def test_2():
    """Simple autotest 2"""
    assert oneStep()
    assert twoStep()


@testgear.step
def oneStep():
    assert oneOneStep()
    assert oneTwoStep()
    return True


@testgear.step
def twoStep():
    return True


@testgear.step('step 1.1', 'description')
def oneOneStep():
    return True


@testgear.step('step 2')
def oneTwoStep():
    return True
```

#### Parameterized test

```py
# Parameterized test with a full set of decorators
from os.path import join, dirname

import testgear
from nose2.tools import params

@params(1, 2, 3)
@testgear.workItemIds(627)
@testgear.externalId('param {num}')
@testgear.displayName('param {num}')
@testgear.title('Test with params')
@testgear.description('E2E_autotest')
@testgear.labels('parameters', 'test')
@testgear.links(url='https://dumps.example.com/module/JCP-777')
@testgear.links(url='https://dumps.example.com/module/JCP-777',
              title='JCP-777',
              type=testgear.LinkType.RELATED,
              description='Description of JCP-777')
def test_nums(num):
    assert num < 4
```

# Contributing

You can help to develop the project. Any contributions are **greatly appreciated**.

* If you have suggestions for adding or removing projects, feel free
  to [open an issue](https://github.com/testgear-tms/adapters-python/issues/new) to discuss it, or directly create a pull
  request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through
  the [Code Of Conduct](https://github.com/testgear-tms/adapters-python/blob/master/CODE_OF_CONDUCT.md) before posting
  your first idea as well.

# License

Distributed under the Apache-2.0 License.
See [LICENSE](https://github.com/testgear-tms/adapters-python/blob/master/LICENSE.md) for more information.

