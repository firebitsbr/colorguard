import nose
import logging
import colorguard

import os

bin_location = str(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../binaries-private'))

logging.getLogger("colorguard").setLevel("DEBUG")
logging.getLogger("povsim").setLevel("DEBUG")

cg = colorguard.ColorGuard(os.path.join(bin_location, "tests/i386/CUSTM_00022"), '\xf0EY\xcaAAA')

nose.tools.assert_true(cg.causes_leak())
pov = cg.attempt_pov()
nose.tools.assert_true(pov.test_binary())