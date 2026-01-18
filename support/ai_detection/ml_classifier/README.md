# ML Classifier for AI-Detection

**Purpose**: Machine learning-based AI text detection (10th detection method)  
**Approach**: Ensemble of Random Forest, XGBoost, LSTM, and fine-tuned transformer  
**Target Accuracy**: >95% with <3% false positive rate

---

## Architecture

### Ensemble Components

1. **Random Forest** (baseline, interpretable)
   - 200 decision trees
   - Feature importance analysis
   - Fast inference (<10ms)

2. **Gradient Boosting** (XGBoost)
   - Highest single-model accuracy
   - Handles imbalanced data well
   - Feature interaction capture

3. **LSTM** (sequence modeling)
   - Captures long-range dependencies
   - Sentence-level patterns
   - Temporal dynamics

4. **Transformer** (fine-tuned BERT/RoBERTa)
   - State-of-the-art performance
   - Contextual understanding
   - Transfer learning from academic corpus

### Ensemble Strategy

**Weighted Voting**:
- Random Forest: 20%
- XGBoost: 30%
- LSTM: 20%
- Transformer: 30%

Weights determined by validation set performance.

---

## Training Data

### Target Corpus (25,000 samples)

**Human-Written** (10,000 samples):
- Published papers from OpenAlex API (5,000)
- Dissertation excerpts (2,000)
- Grant proposals (1,000)
- Peer review comments (1,000)
- Preprints from arXiv (1,000)

**AI-Generated** (10,000 samples):
- GPT-4 generated (3,000)
- Claude Sonnet generated (3,000)
- Gemini generated (2,000)
- GPT-3.5 generated (2,000)

**Mixed** (5,000 samples):
- Human-edited AI text (2,500)
- AI-edited human text (2,500)

### Data Collection Pipeline

```bash
# Collect human papers
python data_collection/collect_human_papers.py \
  --source openalex \
  --count 5000 \
  --fields "computer science,psychology,medicine"

# Generate AI samples
python data_collection/generate_ai_text.py \
  --models "gpt4,claude,gemini" \
  --prompts data_collection/academic_prompts.txt

# Create mixed samples
python data_collection/create_mixed_samples.py \
  --human corpus/human_samples.jsonl \
  --ai corpus/ai_samples.jsonl
```

---

## Feature Engineering

### 200+ Features Extracted

#### 1. Linguistic Features (50 features)

**Part-of-Speech Distributions**:
- Noun/verb/adjective ratios
- Function word frequencies
- Modal verb usage
- Passive voice frequency

**Syntactic Complexity**:
- Parse tree depth (average, max, variance)
- Clause density
- Dependency arc length

**Named Entities**:
- Entity density per 100 words
- Entity type distribution
- Proper noun frequency

#### 2. Statistical Features (40 features)

**N-Gram Perplexity**:
- Unigram, bigram, trigram, 4-gram, 5-gram perplexity
- Against academic corpus baseline

**Vocabulary Richness**:
- Type-token ratio (TTR)
- Moving-average TTR
- Hapax legomena frequency
- Dis legomena frequency

**Burstiness**:
- Word repetition patterns
- Bursty vs non-bursty words ratio

#### 3. Stylometric Features (50 features)

**Function Words**:
- Frequencies of 30 most common function words
- Function word variance

**Character N-Grams**:
- Character bigram/trigram frequencies
- Unusual character combinations

**Punctuation**:
- Comma, semicolon, colon, dash frequencies
- Punctuation diversity
- Sentence-ending punctuation patterns

**Sentence Boundaries**:
- Sentence starter patterns
- Sentence ender patterns
- Transition word placement

#### 4. Semantic Features (30 features)

**Word Embeddings**:
- Average cosine similarity within text
- Semantic coherence score
- Topic diversity

**Semantic Flow**:
- Sentence-to-sentence similarity
- Paragraph-to-paragraph similarity
- Topic drift measure

#### 5. Existing Detection Methods (30 features)

From enhanced_detector.py:
- Base detection scores (5)
- Language model scores (4)
- Complexity scores (6)
- Citation scores (7)
- Combined scores (8)

**Total**: 200 features

---

## Training Pipeline

### Phase 1: Data Preparation

```python
# Extract features from corpus
python features/extract_all_features.py \
  --input corpus/ \
  --output features/feature_matrix.csv

# Split data (70/15/15)
python training/split_data.py \
  --features features/feature_matrix.csv \
  --stratify label
```

### Phase 2: Model Training

```python
# Train Random Forest
python models/train_random_forest.py \
  --features features/train.csv \
  --output models/trained/rf_model.pkl

# Train XGBoost
python models/train_xgboost.py \
  --features features/train.csv \
  --output models/trained/xgb_model.pkl

# Train LSTM
python models/train_lstm.py \
  --features features/train.csv \
  --output models/trained/lstm_model.h5

# Train Transformer
python models/train_transformer.py \
  --base_model roberta-base \
  --features features/train.csv \
  --output models/trained/transformer_model/

# Train Ensemble
python training/train_ensemble.py \
  --models models/trained/ \
  --validation features/val.csv \
  --output models/trained/ensemble.pkl
```

### Phase 3: Evaluation

```python
# Evaluate on test set
python training/evaluate.py \
  --model models/trained/ensemble.pkl \
  --test features/test.csv

# Metrics computed:
# - Accuracy
# - Precision/Recall/F1 (per class)
# - ROC-AUC
# - Calibration curves
# - Confusion matrix
# - Feature importance
```

---

## Integration with Existing System

### Add as 10th Detection Method

Modified `support/ai_detection/enhanced_detector.py`:

```python
class EnhancedAITextDetector:
    def __init__(self, config=None, user_profile_path=None, use_ml=True):
        # Existing detectors
        self.base_detector = AITextDetector(config)
        self.language_model = LanguageModel()
        self.complexity_analyzer = ComplexityAnalyzer()
        self.citation_analyzer = CitationAnalyzer()
        
        # NEW: ML classifier
        if use_ml:
            self.ml_classifier = MLClassifier()
    
    def _calculate_enhanced_confidence(self, ...):
        # Original weights
        confidence = (
            0.30 * base_result.overall_confidence +      # 30%
            0.20 * language_result.overall_score +       # 20%
            0.15 * complexity_result.overall_ai_score +  # 15%
            0.10 * citation_result.overall_ai_score +    # 10%
            0.25 * ml_result.confidence                  # 25% NEW
        )
```

### New Ensemble Weights (with ML)

- Base detection (5 methods): 30%
- Language modeling: 20%
- Complexity: 15%
- Citations: 10%
- **ML Classifier: 25%** ← NEW

---

## Performance Targets

### Accuracy Metrics

**On Test Set** (25% of corpus, never seen during training):
- Accuracy: >95%
- Precision (human): >97%
- Precision (AI): >93%
- Recall (human): >95%
- Recall (AI): >95%
- F1 (macro): >95%

**Error Rates**:
- False Positive Rate: <3% (human text flagged as AI)
- False Negative Rate: <5% (AI text flagged as human)

**Calibration**:
- Expected Calibration Error (ECE): <0.05
- Confidence should match actual accuracy

### Inference Performance

- **Latency**: <200ms per 1000-word document
- **Memory**: <500MB RAM
- **Model Size**: <100MB (ensemble combined)

---

## File Structure

```
ml_classifier/
├── README.md (this file)
│
├── data_collection/
│   ├── collect_human_papers.py
│   ├── generate_ai_text.py
│   ├── create_mixed_samples.py
│   └── validate_labels.py
│
├── corpus/
│   ├── human_samples.jsonl (10K samples)
│   ├── ai_samples.jsonl (10K samples)
│   ├── mixed_samples.jsonl (5K samples)
│   └── metadata.json
│
├── features/
│   ├── linguistic_features.py
│   ├── statistical_features.py
│   ├── stylometric_features.py
│   ├── semantic_features.py
│   ├── existing_features.py (from enhanced_detector)
│   └── extract_all_features.py
│
├── models/
│   ├── random_forest.py
│   ├── xgboost_model.py
│   ├── lstm_classifier.py
│   ├── transformer_classifier.py
│   └── ensemble.py
│
├── training/
│   ├── split_data.py
│   ├── train_ensemble.py
│   ├── evaluate.py
│   ├── hyperparameter_tuning.py
│   └── cross_validation.py
│
└── models/trained/ (saved models after training)
```

---

## Usage After Training

```python
from support.ai_detection.ml_classifier.ensemble import MLEnsemble

# Load trained ensemble
classifier = MLEnsemble.load('models/trained/ensemble.pkl')

# Predict on new text
text = "This comprehensive study leverages robust methodologies..."
result = classifier.predict(text)

print(f"AI Confidence: {result.confidence:.1%}")
print(f"Classification: {result.label}")  # 'human' or 'ai'
print(f"Feature importance: {result.top_features[:5]}")
```

### Integrated with Enhanced Detector

```python
from support.ai_detection.enhanced_detector import EnhancedAITextDetector

# ML classifier automatically loaded
detector = EnhancedAITextDetector(use_ml=True)

result = detector.analyze(text)
# ML classifier contributes 25% to overall confidence
```

---

## Training Status

**Current Status**: Design complete, implementation pending

**Next Steps**:
1. Implement data collection pipeline
2. Build feature extraction modules
3. Train baseline Random Forest
4. Train full ensemble
5. Evaluate and tune
6. Integrate with enhanced_detector.py

---

*ML Classifier design: v1.2.0-beta1*  
*Target accuracy: >95%*  
*Target FPR: <3%*
