## This file reverse renames symbols in the wx package to give
## them their wx prefix again, for backwards compatibility.
##
## Generated by ./distrib/build_renamers.py

# This silly stuff here is so the wxPython.wx module doesn't conflict
# with the wx package.  We need to import modules from the wx package
# here, then we'll put the entry back in sys.modules.
import sys
_wx = None
if sys.modules.has_key('wxPython.wx'):
    _wx = sys.modules['wxPython.wx']
    del sys.modules['wxPython.wx']

import wx.wizard

sys.modules['wxPython.wx']
del sys, _wx


# Now assign all the reverse-renamed names:
wxWIZARD_EX_HELPBUTTON = wx.wizard.WIZARD_EX_HELPBUTTON
wxEVT_WIZARD_PAGE_CHANGED = wx.wizard.wxEVT_WIZARD_PAGE_CHANGED
wxEVT_WIZARD_PAGE_CHANGING = wx.wizard.wxEVT_WIZARD_PAGE_CHANGING
wxEVT_WIZARD_CANCEL = wx.wizard.wxEVT_WIZARD_CANCEL
wxEVT_WIZARD_HELP = wx.wizard.wxEVT_WIZARD_HELP
wxEVT_WIZARD_FINISHED = wx.wizard.wxEVT_WIZARD_FINISHED
wxWizardEvent = wx.wizard.WizardEvent
wxWizardPage = wx.wizard.WizardPage
wxPrePyWizardPage = wx.wizard.PrePyWizardPage
wxPyWizardPage = wx.wizard.PyWizardPage
wxPreWizardPageSimple = wx.wizard.PreWizardPageSimple
wxWizardPageSimple_Chain = wx.wizard.WizardPageSimple_Chain
wxWizardPageSimple = wx.wizard.WizardPageSimple
wxPreWizard = wx.wizard.PreWizard
wxWizard = wx.wizard.Wizard


