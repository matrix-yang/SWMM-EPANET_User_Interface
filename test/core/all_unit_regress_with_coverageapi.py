# TODO: has trouble with cov.exclude using coverageapi, api generated coverage report under htmlcov is not used
import os
import coverage
import webbrowser
import unittest
import test.HTMLTestRunner
import test.core.epanet.test_all
import test.core.swmm.test_all
import test.core.epanet.epanetregressiontest
import test.core.swmm.swmmregressiontest

my_suite = unittest.TestSuite()
my_suite.addTests(test.core.epanet.test_all.my_suite)
my_suite.addTests(test.core.swmm.test_all.my_suite)

if __name__ == "__main__":
    # execute only if run as a script
    report_filename = "test_results_core.html"
    fp = file(report_filename, 'wb')
    runner = test.HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='SWMM-EPANET Core Test Report',
        description='Unit test results')

    # Create a coverage instance
    cov = coverage.Coverage()
    cov.exclude('^\s*(import|from)\s')  # exclude import statements

    cov.start()

    # Run unit tests
    runner.run(my_suite)

    fp.close()

    # Open unit_test reports
    try:
        webbrowser.open_new_tab(report_filename)
    except:
        print("Test results written to " + report_filename)

    # Run EPANET regression test
    reg_epanet = test.core.epanet.epanetregressiontest.EPANETRegressionTest()
    reg_epanet.runTest()

    # Run SWMM regression test
    reg_swmm = test.core.swmm.swmmregressiontest.SWMMRegressionTest()
    reg_swmm.runTest()

    cov.stop()
    cov.save()
    cov.html_report()

    # Open coverage report
    current_path = os.getcwd()
    full_file_path = os.path.join(current_path, 'htmlcov')
    full_file_name = os.path.join(full_file_path, 'index.html')
    try:
        webbrowser.open_new_tab(full_file_name)
    except:
        print("Error opening coverage results")

    # Open unit_test reports
    try:
        webbrowser.open_new_tab(report_filename)
    except:
        print("Test results written to " + report_filename)