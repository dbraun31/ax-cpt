#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on May 30, 2019, at 12:22
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
    originPath='C:\\Users\\alici\\Documents\\ax-cpt-master\\ax-cpt_lastrun.py',
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

# Initialize components for Routine "start0"
start0Clock = core.Clock()
count = 0
Welcome = visual.TextStim(win=win, name='Welcome',
    text='Welcome to the experiment!\n\nTry to relax and find a comfortable, neutral position before we begin.\n\nPress the space bar to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
from pylsl import StreamInfo, StreamOutlet # import required classes
info = StreamInfo(name='Trigger', type='Markers', channel_count=1,
channel_format='int32', source_id='Example') # sets variables for object info
outlet = StreamOutlet(info) # initialize stream.


# Initialize components for Routine "start1"
start1Clock = core.Clock()
basicOverview = visual.TextStim(win=win, name='basicOverview',
    text='In this task, you will be responding to pairs of letters as quickly and accurately as possible.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "start2"
start2Clock = core.Clock()
basicOverview1 = visual.TextStim(win=win, name='basicOverview1',
    text='On each trial, you will:\n\n- See a first letter presented in the center of the screen\n- Wait during a long pause\n- See a second letter presented in three positions across the middle of the display\n\nYou should respond to each letter.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "start3"
start3Clock = core.Clock()
basicOverview2 = visual.TextStim(win=win, name='basicOverview2',
    text='Your main objective is to detect the letter pair "A-X".\n\nFor each pair of letters:\n\n- Always press button 1 when the first letter appears\n\n- For the second letter, if and only if the second letter you see on the screen is an X, and the previous letter was an A, press button 2.\n\nIf you do not see the A-X pair, you should:\n\n- Press button 1 when the first letter appears\n\n- Press button 1 if the second letter you see does not complete the A-X pair',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "start4"
start4Clock = core.Clock()
basicOverview3 = visual.TextStim(win=win, name='basicOverview3',
    text='In some instances, the second letter will not be a letter at all, but a number. \n\nIn these cases, do not press either button 1 or 2. Simply wait for the number to disappear.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "start5"
start5Clock = core.Clock()
basicOverview4 = visual.TextStim(win=win, name='basicOverview4',
    text='You only have 1 second to respond to each letter, so you should respond as quickly and accurately as possible. \n\nYou may still make a response even if the letter disappears off the screen.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "start6"
start6Clock = core.Clock()
blockStart = 0
examples = visual.TextStim(win=win, name='examples',
    text='Here are a few examples to help you understand the task.\n\nFirst trial: You see an A, there is a long delay, you see an X.\nYou should press button 1 when the A appears,\nand button 2 when the X appears.\n\nSecond trial: You see a B, there is a long delay, you see an X.\nYou should press button 1 when the B appears,\nand button 1 when the X appears.\n\nThird trial: You see an A, there is a long delay, you see a 6.\nYou should press button 1 when the A appears, and not respond at all when you see the 6.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "blockStart"
blockStartClock = core.Clock()
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

# ------Prepare to start Routine "start0"-------
t = 0
start0Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
moreInstructions0 = keyboard.Keyboard()
# keep track of which components have finished
start0Components = [Welcome, moreInstructions0]
for thisComponent in start0Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "start0"-------
while continueRoutine:
    # get current time
    t = start0Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome* updates
    if t >= 0.0 and Welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        Welcome.tStart = t  # not accounting for scr refresh
        Welcome.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Welcome, 'tStartRefresh')  # time at next scr refresh
        Welcome.setAutoDraw(True)
    
    # *moreInstructions0* updates
    if t >= 0.0 and moreInstructions0.status == NOT_STARTED:
        # keep track of start time/frame for later
        moreInstructions0.tStart = t  # not accounting for scr refresh
        moreInstructions0.frameNStart = frameN  # exact frame index
        win.timeOnFlip(moreInstructions0, 'tStartRefresh')  # time at next scr refresh
        moreInstructions0.status = STARTED
        # keyboard checking is just starting
        moreInstructions0.clearEvents(eventType='keyboard')
    if moreInstructions0.status == STARTED:
        theseKeys = moreInstructions0.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in start0Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start0"-------
for thisComponent in start0Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welcome.started', Welcome.tStartRefresh)
thisExp.addData('Welcome.stopped', Welcome.tStopRefresh)
# the Routine "start0" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start1"-------
t = 0
start1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = keyboard.Keyboard()
# keep track of which components have finished
start1Components = [basicOverview, key_resp_3]
for thisComponent in start1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "start1"-------
while continueRoutine:
    # get current time
    t = start1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *basicOverview* updates
    if t >= 0.0 and basicOverview.status == NOT_STARTED:
        # keep track of start time/frame for later
        basicOverview.tStart = t  # not accounting for scr refresh
        basicOverview.frameNStart = frameN  # exact frame index
        win.timeOnFlip(basicOverview, 'tStartRefresh')  # time at next scr refresh
        basicOverview.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # not accounting for scr refresh
        key_resp_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in start1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start1"-------
for thisComponent in start1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('basicOverview.started', basicOverview.tStartRefresh)
thisExp.addData('basicOverview.stopped', basicOverview.tStopRefresh)
# the Routine "start1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start2"-------
t = 0
start2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = keyboard.Keyboard()
# keep track of which components have finished
start2Components = [basicOverview1, key_resp_4]
for thisComponent in start2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "start2"-------
while continueRoutine:
    # get current time
    t = start2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *basicOverview1* updates
    if t >= 0.0 and basicOverview1.status == NOT_STARTED:
        # keep track of start time/frame for later
        basicOverview1.tStart = t  # not accounting for scr refresh
        basicOverview1.frameNStart = frameN  # exact frame index
        win.timeOnFlip(basicOverview1, 'tStartRefresh')  # time at next scr refresh
        basicOverview1.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # not accounting for scr refresh
        key_resp_4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in start2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start2"-------
for thisComponent in start2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('basicOverview1.started', basicOverview1.tStartRefresh)
thisExp.addData('basicOverview1.stopped', basicOverview1.tStopRefresh)
# the Routine "start2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start3"-------
t = 0
start3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = keyboard.Keyboard()
# keep track of which components have finished
start3Components = [basicOverview2, key_resp_5]
for thisComponent in start3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "start3"-------
while continueRoutine:
    # get current time
    t = start3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *basicOverview2* updates
    if t >= 0.0 and basicOverview2.status == NOT_STARTED:
        # keep track of start time/frame for later
        basicOverview2.tStart = t  # not accounting for scr refresh
        basicOverview2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(basicOverview2, 'tStartRefresh')  # time at next scr refresh
        basicOverview2.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # not accounting for scr refresh
        key_resp_5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        key_resp_5.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in start3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start3"-------
for thisComponent in start3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('basicOverview2.started', basicOverview2.tStartRefresh)
thisExp.addData('basicOverview2.stopped', basicOverview2.tStopRefresh)
# the Routine "start3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start4"-------
t = 0
start4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = keyboard.Keyboard()
# keep track of which components have finished
start4Components = [basicOverview3, key_resp_6]
for thisComponent in start4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "start4"-------
while continueRoutine:
    # get current time
    t = start4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *basicOverview3* updates
    if t >= 0.0 and basicOverview3.status == NOT_STARTED:
        # keep track of start time/frame for later
        basicOverview3.tStart = t  # not accounting for scr refresh
        basicOverview3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(basicOverview3, 'tStartRefresh')  # time at next scr refresh
        basicOverview3.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # not accounting for scr refresh
        key_resp_6.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        key_resp_6.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in start4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start4"-------
for thisComponent in start4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('basicOverview3.started', basicOverview3.tStartRefresh)
thisExp.addData('basicOverview3.stopped', basicOverview3.tStopRefresh)
# the Routine "start4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start5"-------
t = 0
start5Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = keyboard.Keyboard()
# keep track of which components have finished
start5Components = [basicOverview4, key_resp_7]
for thisComponent in start5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "start5"-------
while continueRoutine:
    # get current time
    t = start5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *basicOverview4* updates
    if t >= 0.0 and basicOverview4.status == NOT_STARTED:
        # keep track of start time/frame for later
        basicOverview4.tStart = t  # not accounting for scr refresh
        basicOverview4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(basicOverview4, 'tStartRefresh')  # time at next scr refresh
        basicOverview4.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # not accounting for scr refresh
        key_resp_7.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        key_resp_7.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in start5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start5"-------
for thisComponent in start5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('basicOverview4.started', basicOverview4.tStartRefresh)
thisExp.addData('basicOverview4.stopped', basicOverview4.tStopRefresh)
# the Routine "start5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start6"-------
t = 0
start6Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = keyboard.Keyboard()
# keep track of which components have finished
start6Components = [examples, key_resp_8]
for thisComponent in start6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "start6"-------
while continueRoutine:
    # get current time
    t = start6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *examples* updates
    if t >= 0.0 and examples.status == NOT_STARTED:
        # keep track of start time/frame for later
        examples.tStart = t  # not accounting for scr refresh
        examples.frameNStart = frameN  # exact frame index
        win.timeOnFlip(examples, 'tStartRefresh')  # time at next scr refresh
        examples.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t  # not accounting for scr refresh
        key_resp_8.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        key_resp_8.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in start6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start6"-------
for thisComponent in start6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('examples.started', examples.tStartRefresh)
thisExp.addData('examples.stopped', examples.tStopRefresh)
# the Routine "start6" was not non-slip safe, so reset the non-slip timer
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
    
    # ------Prepare to start Routine "blockStart"-------
    t = 0
    blockStartClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    if blockStart:
        presentText = "You may now take a short rest break.\n\nPress Space Bar to continue."
    else:
        presentText = "In this section of the experiment, you will be asked to perform five task blocks.\n\nBetween blocks you will have the opportunity to take a short break."
        blockStart = 1
        
    
    
    key_resp_9 = keyboard.Keyboard()
    # keep track of which components have finished
    blockStartComponents = [blockStartInstructions, key_resp_9]
    for thisComponent in blockStartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "blockStart"-------
    while continueRoutine:
        # get current time
        t = blockStartClock.getTime()
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
            blockStartInstructions.setText(presentText, log=False)
        
        # *key_resp_9* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t  # not accounting for scr refresh
            key_resp_9.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            key_resp_9.clearEvents(eventType='keyboard')
        if key_resp_9.status == STARTED:
            theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
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
        for thisComponent in blockStartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blockStart"-------
    for thisComponent in blockStartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockLoop.addData('blockStartInstructions.started', blockStartInstructions.tStartRefresh)
    blockLoop.addData('blockStartInstructions.stopped', blockStartInstructions.tStopRefresh)
    # the Routine "blockStart" was not non-slip safe, so reset the non-slip timer
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
            # keep track of which components have finished
            PreCueComponents = [PreCueFixation]
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
                outlet.push_sample(x=[cueMarker])
                
                # keep track of which components have finished
                CUEComponents = [CueStimulus, CueResponse, PreTargetFixation]
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
                ProbeResponse = keyboard.Keyboard()
                outlet.push_sample(x=[targetMarker])
                
                # keep track of which components have finished
                TARGETComponents = [ProbetStimulus, ProbeResponse]
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
                
                ## i'm using this to control number of trials for development
                trialThreshold = 5
                count += 1
                if count == trialThreshold:
                    trialLoop.finished = True
            # completed 1 repeats of 'subTrial'
            
        # completed 1 repeats of 'timingLoop'
        
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
