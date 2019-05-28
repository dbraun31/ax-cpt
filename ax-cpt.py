#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on May 27, 2019, at 22:20
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
    originPath='D:\\OneDrive - Lehigh University\\Research\\By Semester\\Summer 2019\\NCS\\psychopy\\build\\ax-cpt.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
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

# Initialize components for Routine "start"
startClock = core.Clock()
count = 0

# Initialize components for Routine "TCI"
TCIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "CUE"
CUEClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='+ + +',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "TARGET"
TARGETClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start"-------
t = 0
startClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
startComponents = []
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "start" was not non-slip safe, so reset the non-slip timer
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
        
        # ------Prepare to start Routine "TCI"-------
        t = 0
        TCIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        TCIComponents = [text]
        for thisComponent in TCIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "TCI"-------
        while continueRoutine:
            # get current time
            t = TCIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t  # not accounting for scr refresh
                text.frameNStart = frameN  # exact frame index
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            frameRemains = 0.0 + PreCueTime- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TCIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TCI"-------
        for thisComponent in TCIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        timingLoop.addData('text.started', text.tStartRefresh)
        timingLoop.addData('text.stopped', text.tStopRefresh)
        # the Routine "TCI" was not non-slip safe, so reset the non-slip timer
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
            text_2.setText(Cue)
            key_resp = keyboard.Keyboard()
            # keep track of which components have finished
            CUEComponents = [text_2, key_resp, text_4]
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
                
                # *text_2* updates
                if t >= 0.0 and text_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_2.tStart = t  # not accounting for scr refresh
                    text_2.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_2.status == STARTED and t >= frameRemains:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(False)
                
                # *key_resp* updates
                if t >= 0.0 and key_resp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp.tStart = t  # not accounting for scr refresh
                    key_resp.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                    key_resp.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                    key_resp.clearEvents(eventType='keyboard')
                frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if key_resp.status == STARTED and t >= frameRemains:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
                if key_resp.status == STARTED:
                    theseKeys = key_resp.getKeys(keyList=['1'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        
                        # check for quit:
                        if "escape" == theseKeys:
                            endExpNow = True
                        key_resp.keys = theseKeys.name  # just the last key pressed
                        key_resp.rt = theseKeys.rt
                
                # *text_4* updates
                if t >= .5 and text_4.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_4.tStart = t  # not accounting for scr refresh
                    text_4.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(True)
                frameRemains = .5 + ISI- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_4.status == STARTED and t >= frameRemains:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(False)
                
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
            subTrial.addData('text_2.started', text_2.tStartRefresh)
            subTrial.addData('text_2.stopped', text_2.tStopRefresh)
            # check responses
            if key_resp.keys in ['', [], None]:  # No response was made
                key_resp.keys = None
            subTrial.addData('key_resp.keys',key_resp.keys)
            if key_resp.keys != None:  # we had a response
                subTrial.addData('key_resp.rt', key_resp.rt)
            subTrial.addData('key_resp.started', key_resp.tStartRefresh)
            subTrial.addData('key_resp.stopped', key_resp.tStopRefresh)
            subTrial.addData('text_4.started', text_4.tStartRefresh)
            subTrial.addData('text_4.stopped', text_4.tStopRefresh)
            # the Routine "CUE" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "TARGET"-------
            t = 0
            TARGETClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(1.500000)
            # update component parameters for each repeat
            text_3.setText(Probe)
            key_resp_2 = keyboard.Keyboard()
            # keep track of which components have finished
            TARGETComponents = [text_3, key_resp_2]
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
                
                # *text_3* updates
                if t >= 0.0 and text_3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_3.tStart = t  # not accounting for scr refresh
                    text_3.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    text_3.setAutoDraw(True)
                frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_3.status == STARTED and t >= frameRemains:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                    text_3.setAutoDraw(False)
                
                # *key_resp_2* updates
                if t >= 0.0 and key_resp_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_2.tStart = t  # not accounting for scr refresh
                    key_resp_2.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                    key_resp_2.clearEvents(eventType='keyboard')
                frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if key_resp_2.status == STARTED and t >= frameRemains:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                    key_resp_2.status = FINISHED
                if key_resp_2.status == STARTED:
                    theseKeys = key_resp_2.getKeys(keyList=['1', '2'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        
                        # check for quit:
                        if "escape" == theseKeys:
                            endExpNow = True
                        key_resp_2.keys = theseKeys.name  # just the last key pressed
                        key_resp_2.rt = theseKeys.rt
                
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
            subTrial.addData('text_3.started', text_3.tStartRefresh)
            subTrial.addData('text_3.stopped', text_3.tStopRefresh)
            # check responses
            if key_resp_2.keys in ['', [], None]:  # No response was made
                key_resp_2.keys = None
            subTrial.addData('key_resp_2.keys',key_resp_2.keys)
            if key_resp_2.keys != None:  # we had a response
                subTrial.addData('key_resp_2.rt', key_resp_2.rt)
            subTrial.addData('key_resp_2.started', key_resp_2.tStartRefresh)
            subTrial.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
            subTrial.finished = True
            timingLoop.finished = True
            count += 1
            
            
            subTrial.addData('ISI', ISI)
            subTrial.addData('PreCueTime', PreCueTime)
            subTrial.addData('Probe', Probe)
            subTrial.addData('Cue', Cue)
            
            
            if count == 5:
                trialLoop.finished = True
        # completed 1 repeats of 'subTrial'
        
    # completed 1 repeats of 'timingLoop'
    
    thisExp.nextEntry()
    
# completed 5 repeats of 'trialLoop'


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
