from psychopy import visual, core, event, data, gui
from psychopy.tools.filetools import fromFile, toFile
import numpy, random, csv, os, ast
import sys

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'skew' 
expInfo = {u'session': u'01', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
fileName = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])


#exphandler (easiest way to save the data. Change originPath for specific path on test computer)
thisExp = data.ExperimentHandler(name=expName, version='', extraInfo=expInfo, runtimeInfo=None, originPath=u'/Users/mgreen/Desktop/skew_exp/skew.pyc', savePickle=True, saveWideText=True, dataFileName=fileName)



#create display window (change window size and monitor name for specific monitor!!!)
win = visual.Window([1280,800], fullscr=True, monitor="mgMac", color="white")


#read stimuli csv file 
def getStimInputFile(fileName):
    inputFile = open(fileName, 'rU')
    reader = csv.reader(inputFile, delimiter=',')
    rows = []
    for row in reader:
        rows.append(row)
    inputFile.close()
    return rows

#turn stim file into dictionary of trial info 
def makeTrialDict(listName):
    trialInfo = []
    for row in listName:
        trialInfo.append({'probL':row[0], 'probLpos':ast.literal_eval(row[1]), 'probR':row[2], 'probRpos':ast.literal_eval(row[3]), 'magL':row[4], 'magLpos':ast.literal_eval(row[5]), 'magR':row[6], 'magRpos':ast.literal_eval(row[7])})
    return trialInfo

#practice trials info
practStimInfo = getStimInputFile('practiceTrials.csv')
practTrialInfo = makeTrialDict(practStimInfo)

#real trials info
stimInfo = getStimInputFile('trials.csv')
trialInfo = makeTrialDict(stimInfo)

#Instruction text and window
instructions1 = visual.TextStim(win, text="Welcome to the gambling game!\n \nOn each page, you will see a gamble. your task is to decide whether or not to accept the gamble.", color="black", units='norm') 
instructions2 = visual.TextStim(win, text="The gamble is presented as a pie with each sliver representing the chance of winning or losing money.\n \nThe bigger the slice, the more likely the outcome. The smaller the slice, the less likely the outcome.", color="black", units="norm")
instructions3 = visual.TextStim(win, text="Each slice of the pie will be presented in one corner of the screen.\n \nAbove or below each slice will be the amount of money that you can win or lose.", color='black', units='norm')
instructions4 = visual.TextStim(win, text="Pay attention to the '+' and '-' signs of the gamble.\n \nA '+' means you win that amount of money and a '-' sign means you could lose that amount of money.\n \nAlthough some gambles look similar, they have different signs, so pay attention to the sign.", color="black", units="norm")
instructions5 = visual.TextStim(win, text="One of these choices will be played for real money.\n \nThe outcome of this gamble will determine your final payment.\n \nYou will not know which gamble is played for real money, so please choose the gamble you prefer on each trial.", color="black", units="norm")
instructions6 = visual.TextStim(win, text="To accept the gamble, press the number 1.\n \nTo reject the gamble, press the number 0.", color="black", units="norm")
instructions7 = visual.TextStim(win, text="Remember, there is no right or wrong answer. It is just your personal preference.\n \nDo you have any questions?", color="black", units="norm")


#Instructions
instructions1.draw()
win.update()
event.waitKeys()
instructions2.draw()
win.update()
event.waitKeys()
instructions3.draw()
win.update()
event.waitKeys()
instructions4.draw()
win.update()
event.waitKeys
instructions5.draw()
win.update()
event.waitKeys()
instructions6.draw()
win.update()
event.waitKeys()
instructions7.draw()
win.update()
event.waitKeys()

#initialize practice Trial componenets
startPracticeScreen = visual.TextStim(win, text="You are about to begin the practice trial.\n \nPress the spacebar to begin.", color='black', units='norm')
finishPracticeScreen= visual.TextStim(win, text="You have completed the practice round.\n \nPress the spacebar when you are ready to continue.", color='black', units='norm')
screen_textR = visual.TextStim(win, text=None, color='black', units='norm')
screen_imgR = visual.ImageStim(win, image=None, units='norm')
screen_textL = visual.TextStim(win, text=None, color='black', units='norm')
screen_imgL = visual.ImageStim(win, image=None, units='norm')
fixation = visual.ShapeStim(win, 
    vertices=((0, -0.05), (0, 0.05), (0,0), (-0.025,0), (0.025, 0)),
    lineWidth=5,
    closeShape=False,
    lineColor="black"
)

#start practice trial
startPracticeScreen.draw()
win.flip()
event.waitKeys()
practTrials = data.TrialHandler(practTrialInfo, 1 , method = 'sequential', name='practTrials')
for trial in practTrials:
    fixation.draw()
    win.flip()
    core.wait(1.0)
    screen_textR.setText(trial['magR'])
    screen_textR.setPos(trial['magRpos'])
    screen_textR.draw()
    screen_textL.setText(trial['magL'])
    screen_textL.setPos(trial['magLpos'])
    screen_textL.draw()
    screen_imgR.setImage(trial['probR'])
    screen_imgR.setPos(trial['probRpos'])
    screen_imgR.size = (0.625, 1)
    screen_imgR.draw()
    screen_imgL.setImage(trial['probL'])
    screen_imgL.setPos(trial['probLpos'])
    screen_imgL.size = (0.625, 1)
    screen_imgL.draw()
    win.flip()
    key = event.waitKeys(keyList=['1','0'])
finishPracticeScreen.draw()
win.flip()
event.waitKeys()


#Initialize components for trials
trialClock = core.Clock()
screen_textR = visual.TextStim(win, text=None, color='black', units='norm')
screen_imgR = visual.ImageStim(win, image=None, units='norm')
screen_textL = visual.TextStim(win, text=None, color='black', units='norm')
screen_imgL = visual.ImageStim(win, image=None, units='norm')
fixation = visual.ShapeStim(win, 
    vertices=((0, -0.05), (0, 0.05), (0,0), (-0.025,0), (0.025, 0)),
    lineWidth=5,
    closeShape=False,
    lineColor="black"
)
finishScreen = visual.TextStim(win, text='You have finished the game!\n \nThank you for participating.', color='black', units='norm')

#Trial component
trials = data.TrialHandler(trialInfo, 1 , method = 'random', name='trials', extraInfo=expInfo,)
thisExp.addLoop(trials)
for trial in trials:
    currentLoop = trials
    fixation.draw()
    win.flip()
    core.wait(1.0)
    t = 0
    trialClock.reset()
    resp = event.BuilderKeyResponse()
    
#Clock for response time
    t = trialClock.getTime()
    win.callOnFlip(resp.clock.reset)
    event.clearEvents(eventType='keyboard')
    
#Actual trial
    screen_textR.setText(trial['magR'])
    screen_textR.setPos(trial['magRpos'])
    screen_textR.draw()
    screen_textL.setText(trial['magL'])
    screen_textL.setPos(trial['magLpos'])
    screen_textL.draw()
    screen_imgR.setImage(trial['probR'])
    screen_imgR.setPos(trial['probRpos'])
    screen_imgR.size = (0.625, 1)
    screen_imgR.draw()
    screen_imgL.setImage(trial['probL'])
    screen_imgL.setPos(trial['probLpos'])
    screen_imgL.size = (0.625, 1)
    screen_imgL.draw()
    win.flip()
    key = event.waitKeys(keyList=['1','0'])
    if len(key) > 0:
        resp.keys = key[-1]
        resp.rt = resp.clock.getTime()
    else:
        resp.keys = 'N'
        resp.rt = 'N'
    trials.addData('resp.keys', resp.keys)
    trials.addData('rt', resp.rt)
finishScreen.draw()
win.flip()
event.waitKeys()

#close up and save
trials.saveAsExcel(fileName + '.xlsx', sheetName = 'rawData', stimOut=None, dataOut=['all_raw'])
thisExp.saveAsWideText(fileName + '.csv')
thisExp.abort()
win.close()
core.quit()