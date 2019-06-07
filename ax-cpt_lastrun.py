#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on June 07, 2019, at 16:55
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'ax-cpt'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\dbrau\\OneDrive - Lehigh University\\Research\\By Semester\\Summer 2019\\NCS\\psychopy\\build\\ax-cpt_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='Welcome to the experiment!\n\nTry to relax and find a comfortable, neutral position before we begin.\n\nPress the space bar to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
# Ally added the below code for triggers
from pylsl import StreamInfo, StreamOutlet # import required classes
info = StreamInfo(name='Trigger', type='Markers', channel_count=1,
channel_format='int32', source_id='Example') # sets variables for object info
outlet = StreamOutlet(info) # initialize stream.



# How many trials should there be for the practice block
practiceTrialThreshold = 10

# Do you want to cut the trial loop short (usually for development purposes)?
# If yes, set `cutTrialLoopShort` to True and set the trialThreshold
cutTrialLoopShort = False
trialThreshold = 5
# A counter for cutting the trial loop short
devTrialCount = 0

# Dave added the below code for procedure flow
# For Development, to control how many trials before the experiment ends

# Controls block instructions and practice
practice = 1
firstBlock = 1

# Initialize components for Routine "InstrTrialOverview"
InstrTrialOverviewClock = core.Clock()
InstrTrialOverviewText = visual.TextStim(win=win, name='InstrTrialOverviewText',
    text='In this task, you will be responding to pairs of letters.\n\nOn each trial, you will:\n\n- Wait during a pause while you see a single + sign in the center of the screen\n- See a first letter presented in the center of the screen\n- Wait during a long pause while you see three + signs in the center of the screen\n- See a second letter presented in the center of the screen\n\nYou should respond to these letters as quickly and accurately as possible.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "InstrResponses"
InstrResponsesClock = core.Clock()
InstrResponsesText = visual.TextStim(win=win, name='InstrResponsesText',
    text='Your main objective is to detect the letter pair "A-X" presented in sequence.\n\nFor the first letter that appears\n\n- Always press button 1\n\n\nFor the second letter that appears:\n\n- Press button 1 if the second letter you see does not complete the A-X pair\n\n- Press button 2 if the second letter you see does complete the A-X pair\n\n\nIn some instances, the second letter will not be a letter at all, but a number. \n\nIn these cases, do not press either button 1 or 2. Simply wait for the number to disappear.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "InstrTrialExamples"
InstrTrialExamplesClock = core.Clock()
InstrTrialExamplesText = visual.TextStim(win=win, name='InstrTrialExamplesText',
    text='Here are a few examples to help you understand the task.\n\nFirst trial: You see an A, there is a long delay, you see an X.\nYou should press button 1 when the A appears,\nand button 2 when the X appears.\n\nSecond trial: You see a B, there is a long delay, you see an X.\nYou should press button 1 when the B appears,\nand button 1 when the X appears.\n\nThird trial: You see an A, there is a long delay, you see a 6.\nYou should press button 1 when the A appears, and not respond at all when you see the 6.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "InstrFinalPoints"
InstrFinalPointsClock = core.Clock()
InstrFinalPointsText = visual.TextStim(win=win, name='InstrFinalPointsText',
    text='You only have 1 second to respond to each letter, so you should respond as quickly and accurately as possible. \n\nYou may still make a response even if the letter disappears off the screen.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "BlockStart"
BlockStartClock = core.Clock()
blockStartInstructions = visual.TextStim(win=win, name='blockStartInstructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "PreCue"
PreCueClock = core.Clock()
PreCueFixation = visual.TextStim(win=win, name='PreCueFixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "CUE"
CUEClock = core.Clock()
CueStimulus = visual.TextStim(win=win, name='CueStimulus',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PreTargetFixation = visual.TextStim(win=win, name='PreTargetFixation',
    text='+ + +',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "TARGET"
TARGETClock = core.Clock()
ProbetStimulus = visual.TextStim(win=win, name='ProbetStimulus',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MindWanderingCatch"
MindWanderingCatchClock = core.Clock()
mindWanderingTextDisplay = visual.TextStim(win=win, name='mindWanderingTextDisplay',
    text='Mind wandering text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "allDone"
allDoneClock = core.Clock()
itsAllOver = visual.TextStim(win=win, name='itsAllOver',
    text='This concludes the experiment.\n\nThanks for participating!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
t = 0
WelcomeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
WelcomeResponse = keyboard.Keyboard()
# keep track of which components have finished
WelcomeComponents = [WelcomeText, WelcomeResponse]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeText* updates
    if t >= 0.0 and WelcomeText.status == NOT_STARTED:
        # keep track of start time/frame for later
        WelcomeText.tStart = t  # not accounting for scr refresh
        WelcomeText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(WelcomeText, 'tStartRefresh')  # time at next scr refresh
        WelcomeText.setAutoDraw(True)
    
    # *WelcomeResponse* updates
    if t >= 0.0 and WelcomeResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        WelcomeResponse.tStart = t  # not accounting for scr refresh
        WelcomeResponse.frameNStart = frameN  # exact frame index
        win.timeOnFlip(WelcomeResponse, 'tStartRefresh')  # time at next scr refresh
        WelcomeResponse.status = STARTED
        # keyboard checking is just starting
        WelcomeResponse.clearEvents(eventType='keyboard')
    if WelcomeResponse.status == STARTED:
        theseKeys = WelcomeResponse.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('WelcomeText.started', WelcomeText.tStartRefresh)
thisExp.addData('WelcomeText.stopped', WelcomeText.tStopRefresh)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstrTrialOverview"-------
t = 0
InstrTrialOverviewClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
InstrTrialOverviewResponse = keyboard.Keyboard()
# keep track of which components have finished
InstrTrialOverviewComponents = [InstrTrialOverviewText, InstrTrialOverviewResponse]
for thisComponent in InstrTrialOverviewComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "InstrTrialOverview"-------
while continueRoutine:
    # get current time
    t = InstrTrialOverviewClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrTrialOverviewText* updates
    if t >= 0.0 and InstrTrialOverviewText.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrTrialOverviewText.tStart = t  # not accounting for scr refresh
        InstrTrialOverviewText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(InstrTrialOverviewText, 'tStartRefresh')  # time at next scr refresh
        InstrTrialOverviewText.setAutoDraw(True)
    
    # *InstrTrialOverviewResponse* updates
    if t >= 0.0 and InstrTrialOverviewResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrTrialOverviewResponse.tStart = t  # not accounting for scr refresh
        InstrTrialOverviewResponse.frameNStart = frameN  # exact frame index
        win.timeOnFlip(InstrTrialOverviewResponse, 'tStartRefresh')  # time at next scr refresh
        InstrTrialOverviewResponse.status = STARTED
        # keyboard checking is just starting
        InstrTrialOverviewResponse.clearEvents(eventType='keyboard')
    if InstrTrialOverviewResponse.status == STARTED:
        theseKeys = InstrTrialOverviewResponse.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstrTrialOverviewComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstrTrialOverview"-------
for thisComponent in InstrTrialOverviewComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstrTrialOverviewText.started', InstrTrialOverviewText.tStartRefresh)
thisExp.addData('InstrTrialOverviewText.stopped', InstrTrialOverviewText.tStopRefresh)
# the Routine "InstrTrialOverview" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstrResponses"-------
t = 0
InstrResponsesClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
InstrResponsesResponse = keyboard.Keyboard()
# keep track of which components have finished
InstrResponsesComponents = [InstrResponsesText, InstrResponsesResponse]
for thisComponent in InstrResponsesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "InstrResponses"-------
while continueRoutine:
    # get current time
    t = InstrResponsesClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrResponsesText* updates
    if t >= 0.0 and InstrResponsesText.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrResponsesText.tStart = t  # not accounting for scr refresh
        InstrResponsesText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(InstrResponsesText, 'tStartRefresh')  # time at next scr refresh
        InstrResponsesText.setAutoDraw(True)
    
    # *InstrResponsesResponse* updates
    if t >= 0.0 and InstrResponsesResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrResponsesResponse.tStart = t  # not accounting for scr refresh
        InstrResponsesResponse.frameNStart = frameN  # exact frame index
        win.timeOnFlip(InstrResponsesResponse, 'tStartRefresh')  # time at next scr refresh
        InstrResponsesResponse.status = STARTED
        # keyboard checking is just starting
        InstrResponsesResponse.clearEvents(eventType='keyboard')
    if InstrResponsesResponse.status == STARTED:
        theseKeys = InstrResponsesResponse.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstrResponsesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstrResponses"-------
for thisComponent in InstrResponsesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstrResponsesText.started', InstrResponsesText.tStartRefresh)
thisExp.addData('InstrResponsesText.stopped', InstrResponsesText.tStopRefresh)
# the Routine "InstrResponses" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstrTrialExamples"-------
t = 0
InstrTrialExamplesClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
InstrTrialExamplesResponse = keyboard.Keyboard()
# keep track of which components have finished
InstrTrialExamplesComponents = [InstrTrialExamplesText, InstrTrialExamplesResponse]
for thisComponent in InstrTrialExamplesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "InstrTrialExamples"-------
while continueRoutine:
    # get current time
    t = InstrTrialExamplesClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrTrialExamplesText* updates
    if t >= 0.0 and InstrTrialExamplesText.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrTrialExamplesText.tStart = t  # not accounting for scr refresh
        InstrTrialExamplesText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(InstrTrialExamplesText, 'tStartRefresh')  # time at next scr refresh
        InstrTrialExamplesText.setAutoDraw(True)
    
    # *InstrTrialExamplesResponse* updates
    if t >= 0.0 and InstrTrialExamplesResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrTrialExamplesResponse.tStart = t  # not accounting for scr refresh
        InstrTrialExamplesResponse.frameNStart = frameN  # exact frame index
        win.timeOnFlip(InstrTrialExamplesResponse, 'tStartRefresh')  # time at next scr refresh
        InstrTrialExamplesResponse.status = STARTED
        # keyboard checking is just starting
        InstrTrialExamplesResponse.clearEvents(eventType='keyboard')
    if InstrTrialExamplesResponse.status == STARTED:
        theseKeys = InstrTrialExamplesResponse.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstrTrialExamplesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstrTrialExamples"-------
for thisComponent in InstrTrialExamplesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstrTrialExamplesText.started', InstrTrialExamplesText.tStartRefresh)
thisExp.addData('InstrTrialExamplesText.stopped', InstrTrialExamplesText.tStopRefresh)
# the Routine "InstrTrialExamples" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstrFinalPoints"-------
t = 0
InstrFinalPointsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
InstrFinalPointsResponse = keyboard.Keyboard()
# keep track of which components have finished
InstrFinalPointsComponents = [InstrFinalPointsText, InstrFinalPointsResponse]
for thisComponent in InstrFinalPointsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "InstrFinalPoints"-------
while continueRoutine:
    # get current time
    t = InstrFinalPointsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrFinalPointsText* updates
    if t >= 0.0 and InstrFinalPointsText.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrFinalPointsText.tStart = t  # not accounting for scr refresh
        InstrFinalPointsText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(InstrFinalPointsText, 'tStartRefresh')  # time at next scr refresh
        InstrFinalPointsText.setAutoDraw(True)
    
    # *InstrFinalPointsResponse* updates
    if t >= 0.0 and InstrFinalPointsResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrFinalPointsResponse.tStart = t  # not accounting for scr refresh
        InstrFinalPointsResponse.frameNStart = frameN  # exact frame index
        win.timeOnFlip(InstrFinalPointsResponse, 'tStartRefresh')  # time at next scr refresh
        InstrFinalPointsResponse.status = STARTED
        # keyboard checking is just starting
        InstrFinalPointsResponse.clearEvents(eventType='keyboard')
    if InstrFinalPointsResponse.status == STARTED:
        theseKeys = InstrFinalPointsResponse.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstrFinalPointsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstrFinalPoints"-------
for thisComponent in InstrFinalPointsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstrFinalPointsText.started', InstrFinalPointsText.tStartRefresh)
thisExp.addData('InstrFinalPointsText.stopped', InstrFinalPointsText.tStopRefresh)
# the Routine "InstrFinalPoints" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blockLoop = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blockLoop')
thisExp.addLoop(blockLoop)  # add the loop to the experiment
thisBlockLoop = blockLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
if thisBlockLoop != None:
    for paramName in thisBlockLoop:
        exec('{} = thisBlockLoop[paramName]'.format(paramName))

for thisBlockLoop in blockLoop:
    currentLoop = blockLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
    if thisBlockLoop != None:
        for paramName in thisBlockLoop:
            exec('{} = thisBlockLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "BlockStart"-------
    t = 0
    BlockStartClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if practice:
        blockInstructionText = "Practice instructions"
        practiceTrialCount = 1
        
    
    elif firstBlock:
        blockInstructionText = "In this section of the experiment, you will be asked to perform five task blocks.\n\nBetween blocks you will have the opportunity to take a short break."
        firstBlock = 0
        
    else:
        blockInstructionText = "You may now take a short rest break.\n\nPress Space Bar to continue."
        
        
    
    
    BlockStartResponse = keyboard.Keyboard()
    # keep track of which components have finished
    BlockStartComponents = [blockStartInstructions, BlockStartResponse]
    for thisComponent in BlockStartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "BlockStart"-------
    while continueRoutine:
        # get current time
        t = BlockStartClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blockStartInstructions* updates
        if t >= 0.0 and blockStartInstructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            blockStartInstructions.tStart = t  # not accounting for scr refresh
            blockStartInstructions.frameNStart = frameN  # exact frame index
            win.timeOnFlip(blockStartInstructions, 'tStartRefresh')  # time at next scr refresh
            blockStartInstructions.setAutoDraw(True)
        if blockStartInstructions.status == STARTED:  # only update if drawing
            blockStartInstructions.setText(blockInstructionText, log=False)
        
        # *BlockStartResponse* updates
        if t >= 0.0 and BlockStartResponse.status == NOT_STARTED:
            # keep track of start time/frame for later
            BlockStartResponse.tStart = t  # not accounting for scr refresh
            BlockStartResponse.frameNStart = frameN  # exact frame index
            win.timeOnFlip(BlockStartResponse, 'tStartRefresh')  # time at next scr refresh
            BlockStartResponse.status = STARTED
            # keyboard checking is just starting
            BlockStartResponse.clearEvents(eventType='keyboard')
        if BlockStartResponse.status == STARTED:
            theseKeys = BlockStartResponse.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlockStartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BlockStart"-------
    for thisComponent in BlockStartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockLoop.addData('blockStartInstructions.started', blockStartInstructions.tStartRefresh)
    blockLoop.addData('blockStartInstructions.stopped', blockStartInstructions.tStopRefresh)
    # the Routine "BlockStart" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialLoop = data.TrialHandler(nReps=5, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions/GlobalConditions.xlsx'),
        seed=None, name='trialLoop')
    thisExp.addLoop(trialLoop)  # add the loop to the experiment
    thisTrialLoop = trialLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
    if thisTrialLoop != None:
        for paramName in thisTrialLoop:
            exec('{} = thisTrialLoop[paramName]'.format(paramName))
    
    for thisTrialLoop in trialLoop:
        currentLoop = trialLoop
        # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
        if thisTrialLoop != None:
            for paramName in thisTrialLoop:
                exec('{} = thisTrialLoop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        timingLoop = data.TrialHandler(nReps=1, method='fullRandom', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('conditions\\trialTiming.xlsx'),
            seed=None, name='timingLoop')
        thisExp.addLoop(timingLoop)  # add the loop to the experiment
        thisTimingLoop = timingLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTimingLoop.rgb)
        if thisTimingLoop != None:
            for paramName in thisTimingLoop:
                exec('{} = thisTimingLoop[paramName]'.format(paramName))
        
        for thisTimingLoop in timingLoop:
            currentLoop = timingLoop
            # abbreviate parameter names if possible (e.g. rgb = thisTimingLoop.rgb)
            if thisTimingLoop != None:
                for paramName in thisTimingLoop:
                    exec('{} = thisTimingLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "PreCue"-------
            t = 0
            PreCueClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            MindWanderingResponse = keyboard.Keyboard()
            # Set the mind wandering catch to false to start the trial
            mindWandering = False
            # keep track of which components have finished
            PreCueComponents = [PreCueFixation, MindWanderingResponse]
            for thisComponent in PreCueComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "PreCue"-------
            while continueRoutine:
                # get current time
                t = PreCueClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *PreCueFixation* updates
                if t >= 0.0 and PreCueFixation.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    PreCueFixation.tStart = t  # not accounting for scr refresh
                    PreCueFixation.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(PreCueFixation, 'tStartRefresh')  # time at next scr refresh
                    PreCueFixation.setAutoDraw(True)
                frameRemains = 0.0 + PreCueTime- win.monitorFramePeriod * 0.75  # most of one frame period left
                if PreCueFixation.status == STARTED and t >= frameRemains:
                    # keep track of stop time/frame for later
                    PreCueFixation.tStop = t  # not accounting for scr refresh
                    PreCueFixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PreCueFixation, 'tStopRefresh')  # time at next scr refresh
                    PreCueFixation.setAutoDraw(False)
                
                # *MindWanderingResponse* updates
                if t >= 0.0 and MindWanderingResponse.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    MindWanderingResponse.tStart = t  # not accounting for scr refresh
                    MindWanderingResponse.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(MindWanderingResponse, 'tStartRefresh')  # time at next scr refresh
                    MindWanderingResponse.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(MindWanderingResponse.clock.reset)  # t=0 on next screen flip
                    MindWanderingResponse.clearEvents(eventType='keyboard')
                frameRemains = 0.0 + PreCueTime- win.monitorFramePeriod * 0.75  # most of one frame period left
                if MindWanderingResponse.status == STARTED and t >= frameRemains:
                    # keep track of stop time/frame for later
                    MindWanderingResponse.tStop = t  # not accounting for scr refresh
                    MindWanderingResponse.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(MindWanderingResponse, 'tStopRefresh')  # time at next scr refresh
                    MindWanderingResponse.status = FINISHED
                if MindWanderingResponse.status == STARTED:
                    theseKeys = MindWanderingResponse.getKeys(keyList=['x'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        
                        # check for quit:
                        if "escape" == theseKeys:
                            endExpNow = True
                        if MindWanderingResponse.keys == []:  # then this was the first keypress
                            MindWanderingResponse.keys = theseKeys.name  # just the first key pressed
                            MindWanderingResponse.rt = theseKeys.rt
                            # a response ends the routine
                            continueRoutine = False
                if MindWanderingResponse.keys == 'x':
                    mindWandering = True
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in PreCueComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "PreCue"-------
            for thisComponent in PreCueComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            timingLoop.addData('PreCueFixation.started', PreCueFixation.tStartRefresh)
            timingLoop.addData('PreCueFixation.stopped', PreCueFixation.tStopRefresh)
            # check responses
            if MindWanderingResponse.keys in ['', [], None]:  # No response was made
                MindWanderingResponse.keys = None
            timingLoop.addData('MindWanderingResponse.keys',MindWanderingResponse.keys)
            if MindWanderingResponse.keys != None:  # we had a response
                timingLoop.addData('MindWanderingResponse.rt', MindWanderingResponse.rt)
            timingLoop.addData('MindWanderingResponse.started', MindWanderingResponse.tStartRefresh)
            timingLoop.addData('MindWanderingResponse.stopped', MindWanderingResponse.tStopRefresh)
            # the Routine "PreCue" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            subTrial = data.TrialHandler(nReps=1, method='fullRandom', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions(ConditionFile),
                seed=None, name='subTrial')
            thisExp.addLoop(subTrial)  # add the loop to the experiment
            thisSubTrial = subTrial.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisSubTrial.rgb)
            if thisSubTrial != None:
                for paramName in thisSubTrial:
                    exec('{} = thisSubTrial[paramName]'.format(paramName))
            
            for thisSubTrial in subTrial:
                currentLoop = subTrial
                # abbreviate parameter names if possible (e.g. rgb = thisSubTrial.rgb)
                if thisSubTrial != None:
                    for paramName in thisSubTrial:
                        exec('{} = thisSubTrial[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "CUE"-------
                t = 0
                CUEClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                # update component parameters for each repeat
                CueStimulus.setText(Cue)
                CueResponse = keyboard.Keyboard()
                CueMindWanderingResponse = keyboard.Keyboard()
                outlet.push_sample(x=[cueMarker])
                
                if mindWandering:
                    continueRoutine = False
                # keep track of which components have finished
                CUEComponents = [CueStimulus, CueResponse, PreTargetFixation, CueMindWanderingResponse]
                for thisComponent in CUEComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "CUE"-------
                while continueRoutine:
                    # get current time
                    t = CUEClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *CueStimulus* updates
                    if t >= 0.0 and CueStimulus.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        CueStimulus.tStart = t  # not accounting for scr refresh
                        CueStimulus.frameNStart = frameN  # exact frame index
                        win.timeOnFlip(CueStimulus, 'tStartRefresh')  # time at next scr refresh
                        CueStimulus.setAutoDraw(True)
                    frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if CueStimulus.status == STARTED and t >= frameRemains:
                        # keep track of stop time/frame for later
                        CueStimulus.tStop = t  # not accounting for scr refresh
                        CueStimulus.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(CueStimulus, 'tStopRefresh')  # time at next scr refresh
                        CueStimulus.setAutoDraw(False)
                    
                    # *CueResponse* updates
                    if t >= 0.0 and CueResponse.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        CueResponse.tStart = t  # not accounting for scr refresh
                        CueResponse.frameNStart = frameN  # exact frame index
                        win.timeOnFlip(CueResponse, 'tStartRefresh')  # time at next scr refresh
                        CueResponse.status = STARTED
                        # keyboard checking is just starting
                        win.callOnFlip(CueResponse.clock.reset)  # t=0 on next screen flip
                        CueResponse.clearEvents(eventType='keyboard')
                    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if CueResponse.status == STARTED and t >= frameRemains:
                        # keep track of stop time/frame for later
                        CueResponse.tStop = t  # not accounting for scr refresh
                        CueResponse.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(CueResponse, 'tStopRefresh')  # time at next scr refresh
                        CueResponse.status = FINISHED
                    if CueResponse.status == STARTED:
                        theseKeys = CueResponse.getKeys(keyList=['1'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            if CueResponse.keys == []:  # then this was the first keypress
                                CueResponse.keys = theseKeys.name  # just the first key pressed
                                CueResponse.rt = theseKeys.rt
                    
                    # *PreTargetFixation* updates
                    if t >= .5 and PreTargetFixation.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        PreTargetFixation.tStart = t  # not accounting for scr refresh
                        PreTargetFixation.frameNStart = frameN  # exact frame index
                        win.timeOnFlip(PreTargetFixation, 'tStartRefresh')  # time at next scr refresh
                        PreTargetFixation.setAutoDraw(True)
                    frameRemains = .5 + ISI- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if PreTargetFixation.status == STARTED and t >= frameRemains:
                        # keep track of stop time/frame for later
                        PreTargetFixation.tStop = t  # not accounting for scr refresh
                        PreTargetFixation.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(PreTargetFixation, 'tStopRefresh')  # time at next scr refresh
                        PreTargetFixation.setAutoDraw(False)
                    
                    # *CueMindWanderingResponse* updates
                    if t >= 0.0 and CueMindWanderingResponse.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        CueMindWanderingResponse.tStart = t  # not accounting for scr refresh
                        CueMindWanderingResponse.frameNStart = frameN  # exact frame index
                        win.timeOnFlip(CueMindWanderingResponse, 'tStartRefresh')  # time at next scr refresh
                        CueMindWanderingResponse.status = STARTED
                        # keyboard checking is just starting
                        win.callOnFlip(CueMindWanderingResponse.clock.reset)  # t=0 on next screen flip
                        CueMindWanderingResponse.clearEvents(eventType='keyboard')
                    frameRemains = 0.0 + ISI + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if CueMindWanderingResponse.status == STARTED and t >= frameRemains:
                        # keep track of stop time/frame for later
                        CueMindWanderingResponse.tStop = t  # not accounting for scr refresh
                        CueMindWanderingResponse.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(CueMindWanderingResponse, 'tStopRefresh')  # time at next scr refresh
                        CueMindWanderingResponse.status = FINISHED
                    if CueMindWanderingResponse.status == STARTED:
                        theseKeys = CueMindWanderingResponse.getKeys(keyList=['x'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            if CueMindWanderingResponse.keys == []:  # then this was the first keypress
                                CueMindWanderingResponse.keys = theseKeys.name  # just the first key pressed
                                CueMindWanderingResponse.rt = theseKeys.rt
                                # a response ends the routine
                                continueRoutine = False
                    if CueMindWanderingResponse.keys == 'x':
                        mindWandering = True
                        continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in CUEComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "CUE"-------
                for thisComponent in CUEComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                subTrial.addData('CueStimulus.started', CueStimulus.tStartRefresh)
                subTrial.addData('CueStimulus.stopped', CueStimulus.tStopRefresh)
                # check responses
                if CueResponse.keys in ['', [], None]:  # No response was made
                    CueResponse.keys = None
                subTrial.addData('CueResponse.keys',CueResponse.keys)
                if CueResponse.keys != None:  # we had a response
                    subTrial.addData('CueResponse.rt', CueResponse.rt)
                subTrial.addData('CueResponse.started', CueResponse.tStartRefresh)
                subTrial.addData('CueResponse.stopped', CueResponse.tStopRefresh)
                subTrial.addData('PreTargetFixation.started', PreTargetFixation.tStartRefresh)
                subTrial.addData('PreTargetFixation.stopped', PreTargetFixation.tStopRefresh)
                # check responses
                if CueMindWanderingResponse.keys in ['', [], None]:  # No response was made
                    CueMindWanderingResponse.keys = None
                subTrial.addData('CueMindWanderingResponse.keys',CueMindWanderingResponse.keys)
                if CueMindWanderingResponse.keys != None:  # we had a response
                    subTrial.addData('CueMindWanderingResponse.rt', CueMindWanderingResponse.rt)
                subTrial.addData('CueMindWanderingResponse.started', CueMindWanderingResponse.tStartRefresh)
                subTrial.addData('CueMindWanderingResponse.stopped', CueMindWanderingResponse.tStopRefresh)
                # the Routine "CUE" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "TARGET"-------
                t = 0
                TARGETClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                routineTimer.add(1.500000)
                # update component parameters for each repeat
                ProbetStimulus.setText(Probe)
                ProbeMindWanderingResponse = keyboard.Keyboard()
                ProbeResponse = keyboard.Keyboard()
                outlet.push_sample(x=[targetMarker])
                
                if mindWandering:
                    continueRoutine = False
                # keep track of which components have finished
                TARGETComponents = [ProbetStimulus, ProbeMindWanderingResponse, ProbeResponse]
                for thisComponent in TARGETComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "TARGET"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = TARGETClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *ProbetStimulus* updates
                    if t >= 0.0 and ProbetStimulus.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        ProbetStimulus.tStart = t  # not accounting for scr refresh
                        ProbetStimulus.frameNStart = frameN  # exact frame index
                        win.timeOnFlip(ProbetStimulus, 'tStartRefresh')  # time at next scr refresh
                        ProbetStimulus.setAutoDraw(True)
                    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if ProbetStimulus.status == STARTED and t >= frameRemains:
                        # keep track of stop time/frame for later
                        ProbetStimulus.tStop = t  # not accounting for scr refresh
                        ProbetStimulus.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ProbetStimulus, 'tStopRefresh')  # time at next scr refresh
                        ProbetStimulus.setAutoDraw(False)
                    
                    # *ProbeMindWanderingResponse* updates
                    if t >= 0.0 and ProbeMindWanderingResponse.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        ProbeMindWanderingResponse.tStart = t  # not accounting for scr refresh
                        ProbeMindWanderingResponse.frameNStart = frameN  # exact frame index
                        win.timeOnFlip(ProbeMindWanderingResponse, 'tStartRefresh')  # time at next scr refresh
                        ProbeMindWanderingResponse.status = STARTED
                        # keyboard checking is just starting
                        win.callOnFlip(ProbeMindWanderingResponse.clock.reset)  # t=0 on next screen flip
                        ProbeMindWanderingResponse.clearEvents(eventType='keyboard')
                    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if ProbeMindWanderingResponse.status == STARTED and t >= frameRemains:
                        # keep track of stop time/frame for later
                        ProbeMindWanderingResponse.tStop = t  # not accounting for scr refresh
                        ProbeMindWanderingResponse.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ProbeMindWanderingResponse, 'tStopRefresh')  # time at next scr refresh
                        ProbeMindWanderingResponse.status = FINISHED
                    if ProbeMindWanderingResponse.status == STARTED:
                        theseKeys = ProbeMindWanderingResponse.getKeys(keyList=['x'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            if ProbeMindWanderingResponse.keys == []:  # then this was the first keypress
                                ProbeMindWanderingResponse.keys = theseKeys.name  # just the first key pressed
                                ProbeMindWanderingResponse.rt = theseKeys.rt
                                # a response ends the routine
                                continueRoutine = False
                    
                    # *ProbeResponse* updates
                    if t >= 0.0 and ProbeResponse.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        ProbeResponse.tStart = t  # not accounting for scr refresh
                        ProbeResponse.frameNStart = frameN  # exact frame index
                        win.timeOnFlip(ProbeResponse, 'tStartRefresh')  # time at next scr refresh
                        ProbeResponse.status = STARTED
                        # keyboard checking is just starting
                        win.callOnFlip(ProbeResponse.clock.reset)  # t=0 on next screen flip
                        ProbeResponse.clearEvents(eventType='keyboard')
                    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if ProbeResponse.status == STARTED and t >= frameRemains:
                        # keep track of stop time/frame for later
                        ProbeResponse.tStop = t  # not accounting for scr refresh
                        ProbeResponse.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ProbeResponse, 'tStopRefresh')  # time at next scr refresh
                        ProbeResponse.status = FINISHED
                    if ProbeResponse.status == STARTED:
                        theseKeys = ProbeResponse.getKeys(keyList=['1', '2'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            if ProbeResponse.keys == []:  # then this was the first keypress
                                ProbeResponse.keys = theseKeys.name  # just the first key pressed
                                ProbeResponse.rt = theseKeys.rt
                                # was this 'correct'?
                                if (ProbeResponse.keys == str(CorrRespTarget)) or (ProbeResponse.keys == CorrRespTarget):
                                    ProbeResponse.corr = 1
                                else:
                                    ProbeResponse.corr = 0
                    if ProbeMindWanderingResponse.keys == 'x':
                        mindWandering = True
                        continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in TARGETComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "TARGET"-------
                for thisComponent in TARGETComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                subTrial.addData('ProbetStimulus.started', ProbetStimulus.tStartRefresh)
                subTrial.addData('ProbetStimulus.stopped', ProbetStimulus.tStopRefresh)
                # check responses
                if ProbeMindWanderingResponse.keys in ['', [], None]:  # No response was made
                    ProbeMindWanderingResponse.keys = None
                subTrial.addData('ProbeMindWanderingResponse.keys',ProbeMindWanderingResponse.keys)
                if ProbeMindWanderingResponse.keys != None:  # we had a response
                    subTrial.addData('ProbeMindWanderingResponse.rt', ProbeMindWanderingResponse.rt)
                subTrial.addData('ProbeMindWanderingResponse.started', ProbeMindWanderingResponse.tStartRefresh)
                subTrial.addData('ProbeMindWanderingResponse.stopped', ProbeMindWanderingResponse.tStopRefresh)
                # check responses
                if ProbeResponse.keys in ['', [], None]:  # No response was made
                    ProbeResponse.keys = None
                    # was no response the correct answer?!
                    if str(CorrRespTarget).lower() == 'none':
                       ProbeResponse.corr = 1;  # correct non-response
                    else:
                       ProbeResponse.corr = 0;  # failed to respond (incorrectly)
                # store data for subTrial (TrialHandler)
                subTrial.addData('ProbeResponse.keys',ProbeResponse.keys)
                subTrial.addData('ProbeResponse.corr', ProbeResponse.corr)
                if ProbeResponse.keys != None:  # we had a response
                    subTrial.addData('ProbeResponse.rt', ProbeResponse.rt)
                subTrial.addData('ProbeResponse.started', ProbeResponse.tStartRefresh)
                subTrial.addData('ProbeResponse.stopped', ProbeResponse.tStopRefresh)
                ## force dummy loops to end
                subTrial.finished = True
                timingLoop.finished = True
                
                ## force dummy loops to save out the condition codes
                subTrial.addData('ISI', ISI)
                subTrial.addData('PreCueTime', PreCueTime)
                subTrial.addData('Probe', Probe)
                subTrial.addData('Cue', Cue)
                
                ## Control Practice block
                if practice:
                    practiceTrialCount += 1
                    if practiceTrialCount == practiceTrialThreshold:
                        trialLoop.finished = True
                        practice = 0
                
                ## i'm using this to control number of trials for development
                devTrialCount += 1
                if devTrialCount == trialThreshold and cutTrialLoopShort:
                    trialLoop.finished = True
            # completed 1 repeats of 'subTrial'
            
        # completed 1 repeats of 'timingLoop'
        
        
        # ------Prepare to start Routine "MindWanderingCatch"-------
        t = 0
        MindWanderingCatchClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        if mindWandering == False:
            subTrial.addData("MindWandering", 0)
            continueRoutine = False
            
        else:
            subTrial.addData("MindWandering", 1)
            
        # keep track of which components have finished
        MindWanderingCatchComponents = [mindWanderingTextDisplay]
        for thisComponent in MindWanderingCatchComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "MindWanderingCatch"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = MindWanderingCatchClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *mindWanderingTextDisplay* updates
            if t >= 0.0 and mindWanderingTextDisplay.status == NOT_STARTED:
                # keep track of start time/frame for later
                mindWanderingTextDisplay.tStart = t  # not accounting for scr refresh
                mindWanderingTextDisplay.frameNStart = frameN  # exact frame index
                win.timeOnFlip(mindWanderingTextDisplay, 'tStartRefresh')  # time at next scr refresh
                mindWanderingTextDisplay.setAutoDraw(True)
            frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if mindWanderingTextDisplay.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                mindWanderingTextDisplay.tStop = t  # not accounting for scr refresh
                mindWanderingTextDisplay.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mindWanderingTextDisplay, 'tStopRefresh')  # time at next scr refresh
                mindWanderingTextDisplay.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MindWanderingCatchComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MindWanderingCatch"-------
        for thisComponent in MindWanderingCatchComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trialLoop.addData('mindWanderingTextDisplay.started', mindWanderingTextDisplay.tStartRefresh)
        trialLoop.addData('mindWanderingTextDisplay.stopped', mindWanderingTextDisplay.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 5 repeats of 'trialLoop'
    
# completed 5 repeats of 'blockLoop'


# ------Prepare to start Routine "allDone"-------
t = 0
allDoneClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
allDoneComponents = [itsAllOver]
for thisComponent in allDoneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "allDone"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = allDoneClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *itsAllOver* updates
    if t >= 0.0 and itsAllOver.status == NOT_STARTED:
        # keep track of start time/frame for later
        itsAllOver.tStart = t  # not accounting for scr refresh
        itsAllOver.frameNStart = frameN  # exact frame index
        win.timeOnFlip(itsAllOver, 'tStartRefresh')  # time at next scr refresh
        itsAllOver.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if itsAllOver.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        itsAllOver.tStop = t  # not accounting for scr refresh
        itsAllOver.frameNStop = frameN  # exact frame index
        win.timeOnFlip(itsAllOver, 'tStopRefresh')  # time at next scr refresh
        itsAllOver.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in allDoneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "allDone"-------
for thisComponent in allDoneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('itsAllOver.started', itsAllOver.tStartRefresh)
thisExp.addData('itsAllOver.stopped', itsAllOver.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
