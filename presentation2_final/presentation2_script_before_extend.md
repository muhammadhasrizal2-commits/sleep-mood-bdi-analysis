# Presentation 2: slides, figures and script

**Research question:** what factors can predict whether or not adolescents cross the clinical threshold for depression according to the BDI-II?

**Chosen model:** logistic regression. **Target length:** about 8 minutes (8 slides, about 1 minute each), leaving room under the 10-minute limit.

Each script is about 100–120 words, roughly 50–60 seconds spoken. Figures are in this folder.

| # | Slide | Speaker | Figure | Time |
|---|---|---|---|---|
| 1 | Dataset and research question | Ciara | `slide1_class_balance.png` | 1:00 |
| 2 | Chosen models | Joyce | `slide2_models_f1.png` | 1:00 |
| 3 | Modelling approach | Joyce | `slide3_workflow.png` | 1:00 |
| 4 | Predictions | Saif | `slide4_confusion_matrix.png` | 1:00 |
| 5 | Why the model flags so few | Saif | `slide5_predicted_probabilities.png` | 1:00 |
| 6 | Evaluation | Emily | `slide6_evaluation_metrics.png` | 1:00 |
| 7 | Interpretation: which factors matter | Emily | `slide7_coefficients.png` | 1:00 |
| 8 | Limits and conclusion | Ciara | `slide8_cases_caught.png` | 1:00 |

---

## Slide 1. Dataset and research question (Ciara)

**On the slide**
- Research question (as above)
- 4,810 adolescents; self-reported sleep, screen time and sex
- Target: `depressed` = BDI-II total of 14 or above
- 16.4% above the threshold: imbalanced classes

**Script**
> Our question is what factors can predict whether adolescents cross the clinical threshold for depression on the BDI-II. Our dataset has 4,810 adolescents, with self-reported measures of sleep and screen time, plus sex. Our target is whether the BDI-II total is 14 or above, the cut-off for at least mild depression. As the chart shows, only 787 adolescents, about 16 percent, are above that threshold. This imbalance matters for everything that follows: a model that labels everyone "not depressed" would already be about 84 percent accurate, without learning anything.

## Slide 2. Chosen models (Joyce)

**On the slide**
- Candidates: logistic regression, KNN, stacking (both combined), neural network
- Compared on F1 because the classes are imbalanced
- F1 differences are within the variation between folds
- Chosen: logistic regression (fewest false alarms, interpretable)

**Script**
> We compared several classifiers: logistic regression, K-nearest neighbours, a stacked model combining the two, and a neural network. Because the classes are imbalanced, we compared them on F1, which balances precision and recall, and not on accuracy. The chart shows F1 from five-fold cross-validation, with error bars for the spread between folds. The bars overlap: no model is clearly better. Stacking did not help, because its meta-learner relied almost entirely on logistic regression. So we chose logistic regression. It was tied with the others on F1, it raised about half as many false alarms as KNN or the neural network, and its coefficients let us answer our question about which factors matter.

## Slide 3. Modelling approach (Joyce)

**On the slide**
- Seven features; split 60% train / 20% validation / 20% test
- Scaling inside a pipeline, fitted on training data only (no leakage)
- Models compared with validation data and 5-fold cross-validation
- Test set used once, at the end
- BDI items and total score excluded from features (target leakage)

**Script**
> This is our workflow. We used seven features and split the data into 60 percent training, 20 percent validation and 20 percent test. Scaling sits inside a pipeline, so it is fitted on training data only and nothing from the held-out data leaks into the model. We also left out the BDI items and total score as features, because the target is calculated from them; that would be target leakage. We compared the models using the validation set and five-fold cross-validation. The test set of 962 adolescents was kept aside and used once, for the final check.

## Slide 4. Predictions (Saif)

**On the slide**
- Model outputs a probability; 0.5 or above = "depressed"
- 962 unseen adolescents, 146 actually above the threshold
- Flagged 45: 23 correct, 22 false alarms
- Missed 123

**Script**
> Once the model is trained, we give it the 962 adolescents it has never seen. For each one it produces a probability of being above the threshold, and anyone at 0.5 or above is labelled depressed. The model flagged 45 adolescents. 23 of those really were above the threshold, and 22 were false alarms. But 146 adolescents were actually above the threshold, so the model missed 123 of them. It correctly left 794 unflagged. So the model is cautious: when it flags someone it is right about half the time, but it flags very few.

## Slide 5. Why the model flags so few (Saif)

**On the slide**
- Most predicted probabilities are below 0.5, even for depressed adolescents
- The two groups overlap on these features
- The threshold is a choice: at 0.4, 68 flagged and 32 real cases caught

**Script**
> Why so few? This chart shows the predicted probabilities. Grey is adolescents who are not depressed, blue is those who are. Both groups sit mostly on the left: the typical probability for a depressed adolescent is about 0.23, well under the 0.5 line. The two groups overlap, because their sleep and screen profiles are similar, so the model is rarely confident. The threshold is also a choice. If we lowered it to 0.4, the model would flag 68 adolescents and catch 32 real cases instead of 23, at the cost of more false alarms. Emily will now show how we measure that trade-off.

## Slide 6. Evaluation (Emily)

**On the slide**
- Accuracy 0.849 vs baseline 0.848: misleading
- Precision 0.51, recall 0.16, F1 0.24
- Cross-validation agrees (F1 0.22), so the result is stable
- No overfitting: training and test accuracy are close

**Script**
> On the test set, logistic regression has an accuracy of 0.849. That sounds good, but the baseline of always predicting "not depressed" scores 0.848, so accuracy tells us almost nothing here. The other metrics show the real picture. Precision is 0.51: about half of those flagged are real cases. Recall is 0.16: the model finds about one in six adolescents above the threshold. F1, which combines the two, is 0.24. Cross-validation gave a similar F1 of 0.22, so this is a stable result and not luck from one split. Training and test accuracy are also close, so the model is not overfitting. It generalises; it is just not a strong classifier.

## Slide 7. Interpretation: which factors matter (Emily)

**On the slide**
- Strongest: sleep quality index (more sleep problems), then sex (girls)
- Screen time index also raises the probability
- Coefficients show association, not causation

**Script**
> Because we chose logistic regression, we can read its coefficients. The features are standardised, so the bars are comparable. The strongest predictor is the sleep quality index: more sleep problems go with a higher predicted probability of depression. Second is sex: in our data 24 percent of girls are above the threshold, against 9 percent of boys. The screen time index comes third. Leisure screen hours has a negative coefficient, but it overlaps heavily with the screen time index, so we would not read much into its sign. And these are associations in self-reported, cross-sectional data. They do not show that poor sleep causes depression.

## Slide 8. Limits and conclusion (Ciara)

**On the slide**
- Every model misses most real cases (best: 32 of 146)
- The limit is the features, not the model
- Not suitable for screening; useful for showing which factors matter
- Next: richer features; choose a threshold on validation data

**Script**
> Finally, the limits. This chart shows how many of the 146 real cases each model caught. Logistic regression caught 23, and even the neural network caught only 32. When simple and complex models all hit the same ceiling, the limit is the features and not the model: self-reported sleep, screen time and sex are not enough to separate the two groups. So this model is not suitable as a screening tool. What it does tell us is which factors go with a higher risk: poor sleep quality and being a girl. To improve it, we would need richer features, and we would choose the threshold deliberately using validation data. Thank you.

---

## Likely questions

- **Why not the model with the highest F1 (the neural network)?** Its lead is within the variation between folds, it raises twice as many false alarms, and it cannot show which factors matter. Logistic regression with a threshold of 0.4 catches the same 32 cases.
- **Why does the model miss so many?** The two groups overlap on these features; every model tried catches under a quarter of real cases.
- **Isn't 85% accuracy good?** No: predicting "not depressed" for everyone scores the same.
- **Did stacking help?** No. F1 did not improve and the meta-learner gave logistic regression about nine times the weight of KNN.
- **Why F1?** The classes are imbalanced, so accuracy is misleading; F1 balances precision and recall.
