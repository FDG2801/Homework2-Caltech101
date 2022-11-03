# Report (training, test, validation)
## Francesco Di Gangi, PoliTo. s301793

### **First test**

Parameters configurations:
```
NUM_CLASSES = 102 # 101 + 1: There is am extra Background class that should be removed 

BATCH_SIZE = 256     # Higher batch sizes allows for larger learning rates. An empirical heuristic suggests that, when changing
                     # the batch size, learning rate should change by the same factor to have comparable results

#LR = 1e-3            # The initial Learning Rate
LR=0.05
MOMENTUM = 0.9       # Hyperparameter for SGD, keep this at 0.9 when using SGD
WEIGHT_DECAY = 5e-5  # Regularization, you can keep this at the default

#NUM_EPOCHS = 30      # Total number of training epochs (iterations over dataset)
NUM_EPOCHS = 40      # Total number of training epochs (iterations over dataset)
STEP_SIZE = 20       # How many epochs before decreasing learning rate (if using a step-down policy)
GAMMA = 0.1          # Multiplicative factor for learning rate step-down

LOG_FREQUENCY = 10

```
### Results

Training:
```
Starting epoch 1/40, LR = [0.05]
Step 0, Loss 4.624499320983887
Step 10, Loss 4.505307674407959
Starting epoch 2/40, LR = [0.05]
Step 20, Loss 4.395492076873779
Starting epoch 3/40, LR = [0.05]
Step 30, Loss 4.248867034912109
Starting epoch 4/40, LR = [0.05]
Step 40, Loss 4.025461196899414
Starting epoch 5/40, LR = [0.05]
Step 50, Loss 3.7177677154541016
Starting epoch 6/40, LR = [0.05]
Step 60, Loss 3.646036148071289
Starting epoch 7/40, LR = [0.05]
Step 70, Loss 3.6089510917663574
Starting epoch 8/40, LR = [0.05]
Step 80, Loss 3.481309652328491
Starting epoch 9/40, LR = [0.05]
Step 90, Loss 3.429201364517212
Starting epoch 10/40, LR = [0.05]
Step 100, Loss 3.3156449794769287
Starting epoch 11/40, LR = [0.05]
Step 110, Loss 3.1251277923583984
Step 120, Loss 3.3310964107513428
Starting epoch 12/40, LR = [0.05]
Step 130, Loss 2.842160224914551
Starting epoch 13/40, LR = [0.05]
Step 140, Loss 2.554793119430542
Starting epoch 14/40, LR = [0.05]
Step 150, Loss 2.8588104248046875
Starting epoch 15/40, LR = [0.05]
Step 160, Loss 2.584594964981079
Starting epoch 16/40, LR = [0.05]
Step 170, Loss 2.4694952964782715
Starting epoch 17/40, LR = [0.05]
Step 180, Loss 2.5638585090637207
Starting epoch 18/40, LR = [0.05]
Step 190, Loss 2.117896318435669
Starting epoch 19/40, LR = [0.05]
Step 200, Loss 2.0940921306610107
Starting epoch 20/40, LR = [0.05]
Step 210, Loss 2.110910415649414
Starting epoch 21/40, LR = [0.0005000000000000001]
Step 220, Loss 1.7454769611358643
Step 230, Loss 1.5731656551361084
Starting epoch 22/40, LR = [0.005000000000000001]
Step 240, Loss 1.347882628440857
Starting epoch 23/40, LR = [0.005000000000000001]
Step 250, Loss 1.285560965538025
Starting epoch 24/40, LR = [0.005000000000000001]
Step 260, Loss 1.2999267578125
Starting epoch 25/40, LR = [0.005000000000000001]
Step 270, Loss 1.0682345628738403
Starting epoch 26/40, LR = [0.005000000000000001]
Step 280, Loss 1.1104488372802734
Starting epoch 27/40, LR = [0.005000000000000001]
Step 290, Loss 0.8619168996810913
Starting epoch 28/40, LR = [0.005000000000000001]
Step 300, Loss 0.7201761603355408
Starting epoch 29/40, LR = [0.005000000000000001]
Step 310, Loss 0.7427659034729004
Starting epoch 30/40, LR = [0.005000000000000001]
Step 320, Loss 0.7035382986068726
Starting epoch 31/40, LR = [0.005000000000000001]
Step 330, Loss 0.6204915046691895
Step 340, Loss 0.5858858823776245
Starting epoch 32/40, LR = [0.005000000000000001]
Step 350, Loss 0.6079614758491516
Starting epoch 33/40, LR = [0.005000000000000001]
Step 360, Loss 0.5597737431526184
Starting epoch 34/40, LR = [0.005000000000000001]
Step 370, Loss 0.4444374740123749
Starting epoch 35/40, LR = [0.005000000000000001]
Step 380, Loss 0.5784842371940613
Starting epoch 36/40, LR = [0.005000000000000001]
Step 390, Loss 0.38479936122894287
Starting epoch 37/40, LR = [0.005000000000000001]
Step 400, Loss 0.37974920868873596
Starting epoch 38/40, LR = [0.005000000000000001]
Step 410, Loss 0.3630548417568207
Starting epoch 39/40, LR = [0.005000000000000001]
Step 420, Loss 0.311446875333786
Starting epoch 40/40, LR = [0.005000000000000001]
Step 430, Loss 0.18741323053836823
```
Validation Accuracy: 0.44813278008298757

Test Accuracy: 0.4593847217421362

---
### **Second test**

Parameters configuration:
```
NUM_CLASSES = 102 # 101 + 1: There is am extra Background class that should be removed 

BATCH_SIZE = 256     # Higher batch sizes allows for larger learning rates. An empirical heuristic suggests that, when changing
                     # the batch size, learning rate should change by the same factor to have comparable results

#LR = 1e-3            # The initial Learning Rate
LR=0.005
MOMENTUM = 0.9       # Hyperparameter for SGD, keep this at 0.9 when using SGD
WEIGHT_DECAY = 5e-5  # Regularization, you can keep this at the default

#NUM_EPOCHS = 30      # Total number of training epochs (iterations over dataset)
NUM_EPOCHS = 40      # Total number of training epochs (iterations over dataset)
STEP_SIZE = 20       # How many epochs before decreasing learning rate (if using a step-down policy)
GAMMA = 0.1          # Multiplicative factor for learning rate step-down

LOG_FREQUENCY = 10
```
Training result:
```
Starting epoch 1/40, LR = [0.005]
Step 0, Loss 4.625172138214111
Step 10, Loss 4.610489845275879
Starting epoch 2/40, LR = [0.005]
Step 20, Loss 4.594099521636963
Starting epoch 3/40, LR = [0.005]
Step 30, Loss 4.554521560668945
Starting epoch 4/40, LR = [0.005]
Step 40, Loss 4.509557247161865
Starting epoch 5/40, LR = [0.005]
Step 50, Loss 4.33751916885376
Starting epoch 6/40, LR = [0.005]
Step 60, Loss 3.902759552001953
Starting epoch 7/40, LR = [0.005]
Step 70, Loss 3.6932413578033447
Starting epoch 8/40, LR = [0.005]
Step 80, Loss 3.517118215560913
Starting epoch 9/40, LR = [0.005]
Step 90, Loss 3.407332420349121
Starting epoch 10/40, LR = [0.005]
Step 100, Loss 3.55877947807312
Starting epoch 11/40, LR = [0.005]
Step 110, Loss 3.4079017639160156
Step 120, Loss 3.35353684425354
Starting epoch 12/40, LR = [0.005]
Step 130, Loss 3.4902868270874023
Starting epoch 13/40, LR = [0.005]
Step 140, Loss 3.4395627975463867
Starting epoch 14/40, LR = [0.005]
Step 150, Loss 3.352606773376465
Starting epoch 15/40, LR = [0.005]
Step 160, Loss 3.4662303924560547
Starting epoch 16/40, LR = [0.005]
Step 170, Loss 3.3455214500427246
Starting epoch 17/40, LR = [0.005]
Step 180, Loss 3.2641115188598633
Starting epoch 18/40, LR = [0.005]
Step 190, Loss 3.3470020294189453
Starting epoch 19/40, LR = [0.005]
Step 200, Loss 3.192736864089966
Starting epoch 20/40, LR = [0.005]
Step 210, Loss 3.2164793014526367
Starting epoch 21/40, LR = [5e-05]
Step 220, Loss 3.2634425163269043
Step 230, Loss 3.149106025695801
Starting epoch 22/40, LR = [0.0005]
Step 240, Loss 3.18766450881958
Starting epoch 23/40, LR = [0.0005]
Step 250, Loss 3.2585508823394775
Starting epoch 24/40, LR = [0.0005]
Step 260, Loss 3.100024938583374
Starting epoch 25/40, LR = [0.0005]
Step 270, Loss 3.111215114593506
Starting epoch 26/40, LR = [0.0005]
Step 280, Loss 3.0979442596435547
Starting epoch 27/40, LR = [0.0005]
Step 290, Loss 3.3739829063415527
Starting epoch 28/40, LR = [0.0005]
Step 300, Loss 3.078174352645874
Starting epoch 29/40, LR = [0.0005]
Step 310, Loss 3.107543706893921
Starting epoch 30/40, LR = [0.0005]
Step 320, Loss 3.1172475814819336
Starting epoch 31/40, LR = [0.0005]
Step 330, Loss 3.1673474311828613
Step 340, Loss 3.2506086826324463
Starting epoch 32/40, LR = [0.0005]
Step 350, Loss 3.23568058013916
Starting epoch 33/40, LR = [0.0005]
Step 360, Loss 3.008207321166992
Starting epoch 34/40, LR = [0.0005]
Step 370, Loss 3.1252942085266113
Starting epoch 35/40, LR = [0.0005]
Step 380, Loss 3.148782968521118
Starting epoch 36/40, LR = [0.0005]
Step 390, Loss 3.2626688480377197
Starting epoch 37/40, LR = [0.0005]
Step 400, Loss 2.943732500076294
Starting epoch 38/40, LR = [0.0005]
Step 410, Loss 3.082862377166748
Starting epoch 39/40, LR = [0.0005]
Step 420, Loss 2.987257480621338
Starting epoch 40/40, LR = [0.0005]
Step 430, Loss 3.096139907836914
```
Validation Accuracy: 0.25760719225449513

Test Accuracy: 0.25993778085032837

---
### **Third test**

Parameters configuration:
```
DEVICE = 'cuda' # 'cuda' or 'cpu'

NUM_CLASSES = 102 # 101 + 1: There is am extra Background class that should be removed 

BATCH_SIZE = 256     # Higher batch sizes allows for larger learning rates. An empirical heuristic suggests that, when changing
                     # the batch size, learning rate should change by the same factor to have comparable results

#LR = 1e-3            # The initial Learning Rate
**LR=0.05**
MOMENTUM = 0.9       # Hyperparameter for SGD, keep this at 0.9 when using SGD
WEIGHT_DECAY = 5e-5  # Regularization, you can keep this at the default

**NUM_EPOCHS = 30 **     # Total number of training epochs (iterations over dataset)
#NUM_EPOCHS = 40      # Total number of training epochs (iterations over dataset)
STEP_SIZE = 20       # How many epochs before decreasing learning rate (if using a step-down policy)
GAMMA = 0.1          # Multiplicative factor for learning rate step-down

LOG_FREQUENCY = 10
```

Training:
```
Starting epoch 1/30, LR = [0.05]
Step 0, Loss 4.625744342803955
Step 10, Loss 4.48227596282959
Starting epoch 2/30, LR = [0.05]
Step 20, Loss 3.740297555923462
Starting epoch 3/30, LR = [0.05]
Step 30, Loss 3.8830089569091797
Starting epoch 4/30, LR = [0.05]
Step 40, Loss 3.6859560012817383
Starting epoch 5/30, LR = [0.05]
Step 50, Loss 3.516105890274048
Starting epoch 6/30, LR = [0.05]
Step 60, Loss 3.532048225402832
Starting epoch 7/30, LR = [0.05]
Step 70, Loss 3.496356248855591
Starting epoch 8/30, LR = [0.05]
Step 80, Loss 3.491450309753418
Starting epoch 9/30, LR = [0.05]
Step 90, Loss 3.503085136413574
Starting epoch 10/30, LR = [0.05]
Step 100, Loss 3.4287984371185303
Starting epoch 11/30, LR = [0.05]
Step 110, Loss 3.4872183799743652
Step 120, Loss 3.3754539489746094
Starting epoch 12/30, LR = [0.05]
Step 130, Loss 3.4723150730133057
Starting epoch 13/30, LR = [0.05]
Step 140, Loss 3.0702948570251465
Starting epoch 14/30, LR = [0.05]
Step 150, Loss 3.09810209274292
Starting epoch 15/30, LR = [0.05]
Step 160, Loss 3.0605547428131104
Starting epoch 16/30, LR = [0.05]
Step 170, Loss 2.8131542205810547
Starting epoch 17/30, LR = [0.05]
Step 180, Loss 2.9406673908233643
Starting epoch 18/30, LR = [0.05]
Step 190, Loss 2.6332900524139404
Starting epoch 19/30, LR = [0.05]
Step 200, Loss 2.808293104171753
Starting epoch 20/30, LR = [0.05]
Step 210, Loss 2.3485121726989746
Starting epoch 21/30, LR = [0.0005000000000000001]
Step 220, Loss 2.220149040222168
Step 230, Loss 2.211977958679199
Starting epoch 22/30, LR = [0.005000000000000001]
Step 240, Loss 2.023800849914551
Starting epoch 23/30, LR = [0.005000000000000001]
Step 250, Loss 1.949756383895874
Starting epoch 24/30, LR = [0.005000000000000001]
Step 260, Loss 1.8873478174209595
Starting epoch 25/30, LR = [0.005000000000000001]
Step 270, Loss 1.955935001373291
Starting epoch 26/30, LR = [0.005000000000000001]
Step 280, Loss 1.6631395816802979
Starting epoch 27/30, LR = [0.005000000000000001]
Step 290, Loss 1.7536002397537231
Starting epoch 28/30, LR = [0.005000000000000001]
Step 300, Loss 1.9150570631027222
Starting epoch 29/30, LR = [0.005000000000000001]
Step 310, Loss 1.8654088973999023
Starting epoch 30/30, LR = [0.005000000000000001]
Step 320, Loss 1.8181570768356323
```

Validation Accuracy: 0.42012448132780084

Test Accuracy: 0.42378154165226406

---

### **4th test**

Parameters configuration:
```
DEVICE = 'cuda' # 'cuda' or 'cpu'

NUM_CLASSES = 102 # 101 + 1: There is am extra Background class that should be removed 

BATCH_SIZE = 256     # Higher batch sizes allows for larger learning rates. An empirical heuristic suggests that, when changing
                     # the batch size, learning rate should change by the same factor to have comparable results

#LR = 1e-3            # The initial Learning Rate
LR=0.05
MOMENTUM = 0.9       # Hyperparameter for SGD, keep this at 0.9 when using SGD
WEIGHT_DECAY = 5e-5  # Regularization, you can keep this at the default

NUM_EPOCHS = 30      # Total number of training epochs (iterations over dataset)
#NUM_EPOCHS = 40      # Total number of training epochs (iterations over dataset)
STEP_SIZE = 30       # How many epochs before decreasing learning rate (if using a step-down policy)
GAMMA = 0.1          # Multiplicative factor for learning rate step-down

LOG_FREQUENCY = 10
```

Training:
```
Starting epoch 1/30, LR = [0.05]
Step 0, Loss 4.622094631195068
Step 10, Loss 4.492842674255371
Starting epoch 2/30, LR = [0.05]
Step 20, Loss 4.431883811950684
Starting epoch 3/30, LR = [0.05]
Step 30, Loss 4.24015998840332
Starting epoch 4/30, LR = [0.05]
Step 40, Loss 4.0869646072387695
Starting epoch 5/30, LR = [0.05]
Step 50, Loss 3.7321298122406006
Starting epoch 6/30, LR = [0.05]
Step 60, Loss 3.6424872875213623
Starting epoch 7/30, LR = [0.05]
Step 70, Loss 3.592472553253174
Starting epoch 8/30, LR = [0.05]
Step 80, Loss 3.565256357192993
Starting epoch 9/30, LR = [0.05]
Step 90, Loss 3.3297781944274902
Starting epoch 10/30, LR = [0.05]
Step 100, Loss 3.424517869949341
Starting epoch 11/30, LR = [0.05]
Step 110, Loss 3.3345494270324707
Step 120, Loss 2.9647934436798096
Starting epoch 12/30, LR = [0.05]
Step 130, Loss 3.2085134983062744
Starting epoch 13/30, LR = [0.05]
Step 140, Loss 2.961437702178955
Starting epoch 14/30, LR = [0.05]
Step 150, Loss 2.9144768714904785
Starting epoch 15/30, LR = [0.05]
Step 160, Loss 2.772721767425537
Starting epoch 16/30, LR = [0.05]
Step 170, Loss 2.6722021102905273
Starting epoch 17/30, LR = [0.05]
Step 180, Loss 2.4259192943573
Starting epoch 18/30, LR = [0.05]
Step 190, Loss 2.6213173866271973
Starting epoch 19/30, LR = [0.05]
Step 200, Loss 2.0999789237976074
Starting epoch 20/30, LR = [0.05]
Step 210, Loss 2.191847562789917
Starting epoch 21/30, LR = [0.05]
Step 220, Loss 2.0855870246887207
Step 230, Loss 1.9965972900390625
Starting epoch 22/30, LR = [0.05]
Step 240, Loss 2.0612401962280273
Starting epoch 23/30, LR = [0.05]
Step 250, Loss 1.6727019548416138
Starting epoch 24/30, LR = [0.05]
Step 260, Loss 1.6383421421051025
Starting epoch 25/30, LR = [0.05]
Step 270, Loss 1.3998255729675293
Starting epoch 26/30, LR = [0.05]
Step 280, Loss 1.2616249322891235
Starting epoch 27/30, LR = [0.05]
Step 290, Loss 1.3178436756134033
Starting epoch 28/30, LR = [0.05]
Step 300, Loss 1.2459471225738525
Starting epoch 29/30, LR = [0.05]
Step 310, Loss 1.0263335704803467
Starting epoch 30/30, LR = [0.05]
Step 320, Loss 0.6614776253700256
```

Validation Accuracy: 0.42323651452282157

Test Accuracy: 0.42378154165226406

---

