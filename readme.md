for running a test on the code, you can use the following command:
```bash
mkdir build
cd build
cmake -G Ninja ..
ninja lit-test

```
add the tests to the test folder and run the command above to run the tests.

if there are any other file extensions other than mlir make sure to add that to the lit.cfg.py file in the test folder.


