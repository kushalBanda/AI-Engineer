# Jev vs Clef: support triage results

## Accuracy, latency, cost

| model | tickets | errors | category acc | intent acc | p50 ms | p95 ms | cost | cost / 1k tickets |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| jev | 100 | 0 | 94.0% | 94.0% | 559 | 1797 | $0.00535 | $0.0535 |
| clef | 100 | 0 | 96.0% | 88.0% | 771 | 1349 | $0.00638 | $0.0638 |
| clef-flash | 100 | 0 | 97.0% | 90.0% | 718 | 1167 | $0.00335 | $0.0335 |

## Auto-route threshold: category

Share of tickets at or above the confidence threshold, and accuracy on that share.

| model | conf >= 0.5 | conf >= 0.7 | conf >= 0.8 | conf >= 0.9 | conf >= 0.95 |
| --- | --- | --- | --- | --- | --- |
| jev | 99.0% @ 94.9% | 92.0% @ 97.8% | 90.0% @ 100.0% | 90.0% @ 100.0% | 86.0% @ 100.0% |
| clef | 98.0% @ 98.0% | 95.0% @ 98.9% | 90.0% @ 98.9% | 73.0% @ 100.0% | 51.0% @ 100.0% |
| clef-flash | 94.0% @ 98.9% | 85.0% @ 100.0% | 79.0% @ 100.0% | 65.0% @ 100.0% | 38.0% @ 100.0% |

## Auto-route threshold: intent

Share of tickets at or above the confidence threshold, and accuracy on that share.

| model | conf >= 0.5 | conf >= 0.7 | conf >= 0.8 | conf >= 0.9 | conf >= 0.95 |
| --- | --- | --- | --- | --- | --- |
| jev | 97.0% @ 95.9% | 94.0% @ 95.7% | 90.0% @ 96.7% | 88.0% @ 96.6% | 86.0% @ 96.5% |
| clef | 99.0% @ 88.9% | 85.0% @ 95.3% | 77.0% @ 96.1% | 68.0% @ 98.5% | 43.0% @ 100.0% |
| clef-flash | 95.0% @ 92.6% | 87.0% @ 95.4% | 79.0% @ 96.2% | 66.0% @ 100.0% | 42.0% @ 100.0% |

## Calibration: intent

Accuracy inside each confidence bucket. Well calibrated means accuracy sits in the range.

| model | 0.00-0.50 | 0.50-0.70 | 0.70-0.80 | 0.80-0.90 | 0.90-0.95 | 0.95-1.00 |
| --- | --- | --- | --- | --- | --- | --- |
| jev | 33.3% (n=3) | 100.0% (n=3) | 75.0% (n=4) | 100.0% (n=2) | 100.0% (n=2) | 96.5% (n=86) |
| clef | 0.0% (n=1) | 50.0% (n=14) | 87.5% (n=8) | 77.8% (n=9) | 96.0% (n=25) | 100.0% (n=43) |
| clef-flash | 40.0% (n=5) | 62.5% (n=8) | 87.5% (n=8) | 76.9% (n=13) | 100.0% (n=24) | 100.0% (n=42) |

## Agreement on unlabelled questions

| pair | tickets | needs_human agree (p >= 0.5) | mean urgency gap (0-3) |
| --- | --- | --- | --- |
| jev vs clef | 100 | 91.0% | 0.15 |
| jev vs clef-flash | 100 | 81.0% | 0.29 |
| clef vs clef-flash | 100 | 86.0% | 0.25 |
