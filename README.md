# AX-CPT in PscychoPy for NCS

*Author: Dave Braun*  
*Date: May 28, 2019*  

This repository is for the AX-CPT paradigm developed in PsychoPy for NCS.  

**A breakdown of the main files and directories:**  

- `conditions/` - Contains all Excel files that have each condition as a row.  
- `data/` - Where the data gets written to. Right now there is one output from one run through of five trials.  
- `misc/` - Random stuff used to help with figuring out the details of the paradigm.  

- `ax-cpt.py` and `ax-cpt_lastrun.py` - The scripts compiled by PsychoPy. These are slightly different from each other, although I haven't wrapped my exactly why.
- `ax-cpt.psyexp` - The main experiment as a PsychoPy file.

## Logic Behind the Programming

I found most of PsychoPy to be pretty straight forward and similar to EPrime. One major difference and something that's maybe counterintuitive is how closely coupled loops are with conditions. Within the PsychoPy UI, the only way I found to specify conditions is in the properties of a given loop, where you point the loops to Excel files containing the conditions. The best way I found to handle nested conditions (i.e., calling a nested stimulus set based on selection of some superordinate condition) was to create nested loops. So, there is a global conditions Excel file (i.e., `GlobalConditions.xlsx`) that specifies the trial type, and this file is pointed to from the `trialLoop` loop. One of the variables in `GlobalConditions.xlsx` contains as values file paths that point to subordinate Excel files containing the appropriate stimulus sets for a given trial type.  

The nested loop `subTrial` calls the filepath variable from `GlobalConditions.xlsx` to determine which subordinate Excel file is selected for that given trial. In this way, neither `subTrial` nor `timingLoop` are actually loops per se, they are only there to specify conditions. The only "loops" that actually loop are `trialLoop` and `blockLoop`, where `blockLoop` doesn't call a condition file because nothing, as of now, varies between blocks.  

The `nReps` parameter under loop properties is how many times a loop will run exhausting all of its conditions. For example, if you specify `nReps = 1` and there are four conditions specified in the loop, the loop will actually iterate four times. I added custom code that runs at the end of each trial to force the 'dummy' loops (i.e., `subTrial` and `timingLoop`) to end after one interation and not run through all the different stimulus sets that are defined for a given trial type (e.g., not running through *all* the XY stimuli when XY is the trial type). The code, included in the `TARGET` routine, is below:  

```
## force dummy loops to end
subTrial.finished = True
timingLoop.finished = True

## force dummy loops to save out the condition codes
subTrial.addData('ISI', ISI)
subTrial.addData('PreCueTime', PreCueTime)
subTrial.addData('Probe', Probe)
subTrial.addData('Cue', Cue)

```

Please don't hesistate to contact me with any questions -> dab414@lehigh.edu

Best,
Dave

**Triggers**
At the start of the experiment in the `Welcome` routine is in-line code for connecting to lab streaming layer to send triggers to the fnirs machine and to the recording programs. Then in `CUE` and `TARGET` routines, triggers are sent at the onset of each routine and are located in in-line code called `CueTrigger` and `TargetTrigger` respectfully. Cue triggers are numbered 1-6 and target triggers are numbered 7-12. Below is a guide for which numbers related to which Cue-Target patterns. 
   Cue  Target
AX 1     7
AY 2     8
BX 3     9
BY 4     10
AN 5     11
BN 6     12

The routine `MindWanderingCatch` sends trigger number 13 for whenever a participant indicates that they are mind wandering.