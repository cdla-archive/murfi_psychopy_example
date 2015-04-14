#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.00), Tue Apr 14 17:27:06 2015
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'murfi_example'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'test', u'intermittent:1 or realtime:2': u'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=False,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=[800,600], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "pre_scan_instructions"
pre_scan_instructionsClock = core.Clock()
from murfi_activation_communicator import MurfiActivationCommunicator

roi_names = ['mental_math_roi', 'fingertap_roi','audio_roi','visual_roi']

#communicator = MurfiActivationCommunicator('localhost',
communicator = MurfiActivationCommunicator("192.168.25.5",
                                            15001, 100,
                                            roi_names)
communicator.update()

audio_roi= communicator._rois['audio_roi']['activation']
fingertap_roi= communicator._rois['fingertap_roi']['activation']
mental_math_roi= communicator._rois['mental_math_roi']['activation']
visual_roi= communicator._rois['visual_roi']['activation']
audio_roi = audio_roi[~np.isnan(audio_roi)]
fingertap_roi = fingertap[~np.isnan(fingertap_roi)]
mental_math_roi = mental_math[~np.isnan(mental_math)]
visual_roi = visual[~np.isnan(visual)]

text = visual.TextStim(win=win, ori=0, name='text',
    text=u'Please do the following tasks when indicated:\n\nFingertap - tap your fingers while keeping your head still\nMental Math - solve the math problems\nAudio - listen for the audio cue\nVisual - fixate at the center of the checkerboard\n\n\n\nExperimenter press spacebar to continue',    font=u'Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "trigger"
triggerClock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text=u'Waiting for Trigger',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
baseline_text = visual.TextStim(win=win, ori=0, name='baseline_text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
condition = visual.TextStim(win=win, ori=0, name='condition',
    text='default text',    font=u'Arial',
    pos=[0, .7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
cue_image_var = visual.ImageStim(win=win, name='cue_image_var',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
cue_sound_var = sound.Sound('A', secs=-1)
cue_sound_var.setVolume(1.0)
cue_text_var = visual.TextStim(win=win, ori=0, name='cue_text_var',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.25, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0)
feedback_1 = visual.TextStim(win=win, ori=0, name='feedback_1',
    text='default text',    font=u'Arial',
    pos=[-.75, -.7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)
feedback_2 = visual.TextStim(win=win, ori=0, name='feedback_2',
    text='default text',    font=u'Arial',
    pos=[-.25, -.7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0)
feedback_3 = visual.TextStim(win=win, ori=0, name='feedback_3',
    text='default text',    font=u'Arial',
    pos=[.25, -.7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-6.0)
feedback_4 = visual.TextStim(win=win, ori=0, name='feedback_4',
    text='default text',    font=u'Arial',
    pos=[.75, -.7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-7.0)


# Initialize components for Routine "fixation"
fixationClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
ifeedback_1 = visual.TextStim(win=win, ori=0, name='ifeedback_1',
    text='default text',    font=u'Arial',
    pos=[-.75, -.7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
ifeedback_2 = visual.TextStim(win=win, ori=0, name='ifeedback_2',
    text='default text',    font=u'Arial',
    pos=[-.25, -.7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
ifeedback_3 = visual.TextStim(win=win, ori=0, name='ifeedback_3',
    text='default text',    font=u'Arial',
    pos=[.25, -.7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0)
ifeedback_4 = visual.TextStim(win=win, ori=0, name='ifeedback_4',
    text='default text',    font=u'Arial',
    pos=[.75, -.7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)
rfeedback_1 = visual.TextStim(win=win, ori=0, name='rfeedback_1',
    text='default text',    font=u'Arial',
    pos=[-.75, -.7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0)
rfeedback_2 = visual.TextStim(win=win, ori=0, name='rfeedback_2',
    text='default text',    font=u'Arial',
    pos=[-.25, -.7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-6.0)
rfeedback_3 = visual.TextStim(win=win, ori=0, name='rfeedback_3',
    text='default text',    font=u'Arial',
    pos=[.25, -.7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-7.0)
rfeedback_4 = visual.TextStim(win=win, ori=0, name='rfeedback_4',
    text='default text',    font=u'Arial',
    pos=[.75,-.7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-8.0)
from numpy import mean
roi1_average=' '
roi2_average=' '
roi3_average=' '
roi4_average=' '

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "pre_scan_instructions"-------
t = 0
pre_scan_instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
pre_scan_instructionsComponents = []
pre_scan_instructionsComponents.append(text)
pre_scan_instructionsComponents.append(key_resp_2)
for thisComponent in pre_scan_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pre_scan_instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pre_scan_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pre_scan_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "pre_scan_instructions"-------
for thisComponent in pre_scan_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()

#------Prepare to start Routine "trigger"-------
t = 0
triggerClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
trigger_button = event.BuilderKeyResponse()  # create an object of type KeyResponse
trigger_button.status = NOT_STARTED
# keep track of which components have finished
triggerComponents = []
triggerComponents.append(trigger_button)
triggerComponents.append(text_4)
for thisComponent in triggerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "trigger"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = triggerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trigger_button* updates
    if t >= 0.0 and trigger_button.status == NOT_STARTED:
        # keep track of start time/frame for later
        trigger_button.tStart = t  # underestimates by a little under one frame
        trigger_button.frameNStart = frameN  # exact frame index
        trigger_button.status = STARTED
        # keyboard checking is just starting
        trigger_button.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if trigger_button.status == STARTED:
        theseKeys = event.getKeys(keyList=['+', 'num_add', 'r', '5', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            trigger_button.keys = theseKeys[-1]  # just the last key pressed
            trigger_button.rt = trigger_button.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "trigger"-------
for thisComponent in triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trigger_button.keys in ['', [], None]:  # No response was made
   trigger_button.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('trigger_button.keys',trigger_button.keys)
if trigger_button.keys != None:  # we had a response
    thisExp.addData('trigger_button.rt', trigger_button.rt)
thisExp.nextEntry()

#------Prepare to start Routine "baseline"-------
t = 0
baselineClock.reset()  # clock 
frameN = -1
routineTimer.add(30.000000)
# update component parameters for each repeat
# keep track of which components have finished
baselineComponents = []
baselineComponents.append(baseline_text)
for thisComponent in baselineComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "baseline"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = baselineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *baseline_text* updates
    if t >= 0.0 and baseline_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        baseline_text.tStart = t  # underestimates by a little under one frame
        baseline_text.frameNStart = frameN  # exact frame index
        baseline_text.setAutoDraw(True)
    if baseline_text.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
        baseline_text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "baseline"-------
for thisComponent in baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
condition_loop = data.TrialHandler(nReps=8, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'utils/conditions.csv'),
    seed=None, name='condition_loop')
thisExp.addLoop(condition_loop)  # add the loop to the experiment
thisCondition_loop = condition_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisCondition_loop.rgb)
if thisCondition_loop != None:
    for paramName in thisCondition_loop.keys():
        exec(paramName + '= thisCondition_loop.' + paramName)

for thisCondition_loop in condition_loop:
    currentLoop = condition_loop
    # abbreviate parameter names if possible (e.g. rgb = thisCondition_loop.rgb)
    if thisCondition_loop != None:
        for paramName in thisCondition_loop.keys():
            exec(paramName + '= thisCondition_loop.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    repetitions = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(cond_file),
        seed=None, name='repetitions')
    thisExp.addLoop(repetitions)  # add the loop to the experiment
    thisRepetition = repetitions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisRepetition.rgb)
    if thisRepetition != None:
        for paramName in thisRepetition.keys():
            exec(paramName + '= thisRepetition.' + paramName)
    
    for thisRepetition in repetitions:
        currentLoop = repetitions
        # abbreviate parameter names if possible (e.g. rgb = thisRepetition.rgb)
        if thisRepetition != None:
            for paramName in thisRepetition.keys():
                exec(paramName + '= thisRepetition.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        condition.setText(cond)
        cue_image_var.setOpacity(cue_opacity)
        cue_image_var.setImage(cue_image)
        cue_sound_var.setSound(cue_sound)
        cue_sound_var.setVolume(cue_volume)
        cue_text_var.setText(cue_text)
        communicator.update()
        
        if expInfo['intermittent:1 or realtime:2']=='1':
            roi1_score=' '
            roi2_score=' '
            roi3_score=' '
            roi4_score=' '
        elif expInfo['intermittent:1 or realtime:2']=='2':
            roi1_score='audio: \n%.03f'%(float(audio_roi[-1]))
            roi2_score='fingertap: \n%.03f'%(float(fingertap_roi[-1]))
            roi3_score='mental math: \n%.03f'%(float(mental_math_roi[-1]))
            roi4_score='visual: \n%.03f'%(float(visual_roi[-1]))
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(condition)
        trialComponents.append(cue_image_var)
        trialComponents.append(cue_sound_var)
        trialComponents.append(cue_text_var)
        trialComponents.append(feedback_1)
        trialComponents.append(feedback_2)
        trialComponents.append(feedback_3)
        trialComponents.append(feedback_4)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *condition* updates
            if t >= 0.0 and condition.status == NOT_STARTED:
                # keep track of start time/frame for later
                condition.tStart = t  # underestimates by a little under one frame
                condition.frameNStart = frameN  # exact frame index
                condition.setAutoDraw(True)
            if condition.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                condition.setAutoDraw(False)
            
            # *cue_image_var* updates
            if t >= 0.0 and cue_image_var.status == NOT_STARTED:
                # keep track of start time/frame for later
                cue_image_var.tStart = t  # underestimates by a little under one frame
                cue_image_var.frameNStart = frameN  # exact frame index
                cue_image_var.setAutoDraw(True)
            if cue_image_var.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                cue_image_var.setAutoDraw(False)
            # start/stop cue_sound_var
            if t >= 0.0 and cue_sound_var.status == NOT_STARTED:
                # keep track of start time/frame for later
                cue_sound_var.tStart = t  # underestimates by a little under one frame
                cue_sound_var.frameNStart = frameN  # exact frame index
                cue_sound_var.play()  # start the sound (it finishes automatically)
            if cue_sound_var.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                cue_sound_var.stop()  # stop the sound (if longer than duration)
            
            # *cue_text_var* updates
            if t >= 0.0 and cue_text_var.status == NOT_STARTED:
                # keep track of start time/frame for later
                cue_text_var.tStart = t  # underestimates by a little under one frame
                cue_text_var.frameNStart = frameN  # exact frame index
                cue_text_var.setAutoDraw(True)
            if cue_text_var.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                cue_text_var.setAutoDraw(False)
            
            # *feedback_1* updates
            if t >= 0.0 and feedback_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_1.tStart = t  # underestimates by a little under one frame
                feedback_1.frameNStart = frameN  # exact frame index
                feedback_1.setAutoDraw(True)
            if feedback_1.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                feedback_1.setAutoDraw(False)
            if feedback_1.status == STARTED:  # only update if being drawn
                feedback_1.setText(roi1_score, log=False)
            
            # *feedback_2* updates
            if t >= 0.0 and feedback_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_2.tStart = t  # underestimates by a little under one frame
                feedback_2.frameNStart = frameN  # exact frame index
                feedback_2.setAutoDraw(True)
            if feedback_2.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                feedback_2.setAutoDraw(False)
            if feedback_2.status == STARTED:  # only update if being drawn
                feedback_2.setText(roi2_score, log=False)
            
            # *feedback_3* updates
            if t >= 0.0 and feedback_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_3.tStart = t  # underestimates by a little under one frame
                feedback_3.frameNStart = frameN  # exact frame index
                feedback_3.setAutoDraw(True)
            if feedback_3.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                feedback_3.setAutoDraw(False)
            if feedback_3.status == STARTED:  # only update if being drawn
                feedback_3.setText(roi3_score
, log=False)
            
            # *feedback_4* updates
            if t >= 0.0 and feedback_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_4.tStart = t  # underestimates by a little under one frame
                feedback_4.frameNStart = frameN  # exact frame index
                feedback_4.setAutoDraw(True)
            if feedback_4.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                feedback_4.setAutoDraw(False)
            if feedback_4.status == STARTED:  # only update if being drawn
                feedback_4.setText(roi4_score, log=False)
            communicator.update()
            audio_roi= communicator._rois['audio_roi']['activation']
            fingertap_roi= communicator._rois['fingertap_roi']['activation']
            mental_math_roi= communicator._rois['mental_math_roi']['activation']
            visual_roi= communicator._rois['visual_roi']['activation']
            audio_roi = audio_roi[~numpy.isnan(audio_roi)]
            fingertap_roi = fingertap[~numpy.isnan(fingertap_roi)]
            mental_math_roi = mental_math[~numpy.isnan(mental_math)]
            visual_roi = visual[~numpy.isnan(visual)]
            
            if expInfo['intermittent:1 or realtime:2']=='1':
                roi1_score=' '
                roi2_score=' '
                roi3_score=' '
                roi4_score=' '
            elif expInfo['intermittent:1 or realtime:2']=='2':
                roi1_score='audio: \n%.03f'%(float(audio_roi[-1]))
                roi2_score='fingertap: \n%.03f'%(float(fingertap_roi[-1]))
                roi3_score='mental math: \n%.03f'%(float(mental_math_roi[-1]))
                roi4_score='visual: \n%.03f'%(float(visual_roi[-1]))
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        cue_sound_var.stop() #ensure sound has stopped at end of routine
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'repetitions'
    
    
    #------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock 
    frameN = -1
    routineTimer.add(18.000000)
    # update component parameters for each repeat
    communicator.update()
    audio_roi= communicator._rois['audio_roi']['activation']
    fingertap_roi= communicator._rois['fingertap_roi']['activation']
    mental_math_roi= communicator._rois['mental_math_roi']['activation']
    visual_roi= communicator._rois['visual_roi']['activation']
    audio_roi = audio_roi[~np.isnan(audio_roi)]
    fingertap_roi = fingertap[~np.isnan(fingertap_roi)]
    mental_math_roi = mental_math[~np.isnan(mental_math)]
    visual_roi = visual[~np.isnan(visual)]
    
    if expInfo['intermittent:1 or realtime:2']=='1':
        roi1_average='audio: \n%.03f'%(mean([float(x) for x in audio_roi[-18:]]))
        roi2_average='fingertap: \n%.03f'%(mean([float(x) for x in fingertap_roi[-18:]]))
        roi3_average='mental math: \n%.03f'%(mean([float(x) for x in mental_math_roi[-18:]]))
        roi4_average='visual: \n%.03f'%(mean([float(x) for x in visual_roi[-18:]]))
    elif expInfo['intermittent:1 or realtime:2']=='2':
        communicator.update()
        roi1_score='audio: \n%.03f'%(float(audio_roi[-1]))
        roi2_score='fingertap: \n%.03f'%(float(fingertap_roi[-1]))
        roi3_score='mental math: \n%.03f'%(float(mental_math_roi[-1]))
        roi4_score='visual: \n%.03f'%(float(visual_roi[-1]))
    
    # keep track of which components have finished
    fixationComponents = []
    fixationComponents.append(text_3)
    fixationComponents.append(ifeedback_1)
    fixationComponents.append(ifeedback_2)
    fixationComponents.append(ifeedback_3)
    fixationComponents.append(ifeedback_4)
    fixationComponents.append(rfeedback_1)
    fixationComponents.append(rfeedback_2)
    fixationComponents.append(rfeedback_3)
    fixationComponents.append(rfeedback_4)
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fixation"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        if text_3.status == STARTED and t >= (0.0 + (18-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_3.setAutoDraw(False)
        
        # *ifeedback_1* updates
        if t >= 4.0 and ifeedback_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            ifeedback_1.tStart = t  # underestimates by a little under one frame
            ifeedback_1.frameNStart = frameN  # exact frame index
            ifeedback_1.setAutoDraw(True)
        if ifeedback_1.status == STARTED and t >= (4.0 + (4.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            ifeedback_1.setAutoDraw(False)
        if ifeedback_1.status == STARTED:  # only update if being drawn
            ifeedback_1.setText(roi1_average, log=False)
        
        # *ifeedback_2* updates
        if t >= 4.0 and ifeedback_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ifeedback_2.tStart = t  # underestimates by a little under one frame
            ifeedback_2.frameNStart = frameN  # exact frame index
            ifeedback_2.setAutoDraw(True)
        if ifeedback_2.status == STARTED and t >= (4.0 + (4.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            ifeedback_2.setAutoDraw(False)
        if ifeedback_2.status == STARTED:  # only update if being drawn
            ifeedback_2.setText(roi2_average, log=False)
        
        # *ifeedback_3* updates
        if t >= 4.0 and ifeedback_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            ifeedback_3.tStart = t  # underestimates by a little under one frame
            ifeedback_3.frameNStart = frameN  # exact frame index
            ifeedback_3.setAutoDraw(True)
        if ifeedback_3.status == STARTED and t >= (4.0 + (4.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            ifeedback_3.setAutoDraw(False)
        if ifeedback_3.status == STARTED:  # only update if being drawn
            ifeedback_3.setText(roi3_average, log=False)
        
        # *ifeedback_4* updates
        if t >= 4.0 and ifeedback_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            ifeedback_4.tStart = t  # underestimates by a little under one frame
            ifeedback_4.frameNStart = frameN  # exact frame index
            ifeedback_4.setAutoDraw(True)
        if ifeedback_4.status == STARTED and t >= (4.0 + (4.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            ifeedback_4.setAutoDraw(False)
        if ifeedback_4.status == STARTED:  # only update if being drawn
            ifeedback_4.setText(roi4_average, log=False)
        
        # *rfeedback_1* updates
        if t >= 0.0 and rfeedback_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            rfeedback_1.tStart = t  # underestimates by a little under one frame
            rfeedback_1.frameNStart = frameN  # exact frame index
            rfeedback_1.setAutoDraw(True)
        if rfeedback_1.status == STARTED and t >= (0.0 + (18.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            rfeedback_1.setAutoDraw(False)
        if rfeedback_1.status == STARTED:  # only update if being drawn
            rfeedback_1.setText(roi1_score
, log=False)
        
        # *rfeedback_2* updates
        if t >= 0.0 and rfeedback_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rfeedback_2.tStart = t  # underestimates by a little under one frame
            rfeedback_2.frameNStart = frameN  # exact frame index
            rfeedback_2.setAutoDraw(True)
        if rfeedback_2.status == STARTED and t >= (0.0 + (18.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            rfeedback_2.setAutoDraw(False)
        if rfeedback_2.status == STARTED:  # only update if being drawn
            rfeedback_2.setText(roi2_score
, log=False)
        
        # *rfeedback_3* updates
        if t >= 0.0 and rfeedback_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            rfeedback_3.tStart = t  # underestimates by a little under one frame
            rfeedback_3.frameNStart = frameN  # exact frame index
            rfeedback_3.setAutoDraw(True)
        if rfeedback_3.status == STARTED and t >= (0.0 + (18.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            rfeedback_3.setAutoDraw(False)
        if rfeedback_3.status == STARTED:  # only update if being drawn
            rfeedback_3.setText(roi3_score, log=False)
        
        # *rfeedback_4* updates
        if t >= 0.0 and rfeedback_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            rfeedback_4.tStart = t  # underestimates by a little under one frame
            rfeedback_4.frameNStart = frameN  # exact frame index
            rfeedback_4.setAutoDraw(True)
        if rfeedback_4.status == STARTED and t >= (0.0 + (18.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            rfeedback_4.setAutoDraw(False)
        if rfeedback_4.status == STARTED:  # only update if being drawn
            rfeedback_4.setText(roi4_score, log=False)
        communicator.update()
        audio_roi= communicator._rois['audio_roi']['activation']
        fingertap_roi= communicator._rois['fingertap_roi']['activation']
        mental_math_roi= communicator._rois['mental_math_roi']['activation']
        visual_roi= communicator._rois['visual_roi']['activation']
        audio_roi = audio_roi[~np.isnan(audio_roi)]
        fingertap_roi = fingertap[~np.isnan(fingertap_roi)]
        mental_math_roi = mental_math[~np.isnan(mental_math)]
        visual_roi = visual[~np.isnan(visual)]
        
        if expInfo['intermittent:1 or realtime:2']=='2':
            roi1_score='audio: \n%.03f'%(float(audio_roi[-1]))
            roi2_score='fingertap: \n%.03f'%(float(fingertap_roi[-1]))
            roi3_score='mental math: \n%.03f'%(float(mental_math_roi[-1]))
            roi4_score='visual: \n%.03f'%(float(visual_roi[-1]))
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
# completed 8 repeats of 'condition_loop'




win.close()
core.quit()
