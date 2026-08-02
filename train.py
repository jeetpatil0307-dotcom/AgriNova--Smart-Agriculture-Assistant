import os
import json
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Configuration
DATASET_DIR = r"C:\Users\Dell\AgriNova-AI\PlantVillage"
MODELS_DIR = "models"
MODEL_SAVE_PATH = os.path.join(MODELS_DIR, "plant_disease_model.keras")
CLASS_NAMES_SAVE_PATH = os.path.join(MODELS_DIR, "class_names.json")
PLOT_SAVE_PATH = os.path.join(MODELS_DIR, "training_history.png")

IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 25

def main():
    print("=" * 60)
    print("AgriNova AI - Plant Disease Model Training")
    print("=" * 60)

    # Create models directory if it doesn't exist
    os.makedirs(MODELS_DIR, exist_ok=True)

    dataset_path = DATASET_DIR
    if not os.path.exists(dataset_path):
        alt_path = os.path.join(os.path.dirname(__file__), "PlantVillage")
        if os.path.exists(alt_path):
            dataset_path = alt_path
        else:
            raise FileNotFoundError(f"Dataset directory not found at {DATASET_DIR} or {alt_path}")

    print(f"Dataset location: {dataset_path}")

    # 1. ImageDataGenerator (80% Train, 20% Validation, Rescale 0-1, Rotation, Zoom, Horizontal Flip)
    print("\nSetting up ImageDataGenerator (80% Train / 20% Validation split)...")
    datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=25,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=0.2
    )

    print("\nLoading Training Dataset...")
    train_generator = datagen.flow_from_directory(
        dataset_path,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training',
        shuffle=True
    )

    print("Loading Validation Dataset...")
    val_generator = datagen.flow_from_directory(
        dataset_path,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation',
        shuffle=False
    )

    # 2. Save Class Names to models/class_names.json
    class_indices = train_generator.class_indices
    class_names = {str(v): k for k, v in class_indices.items()}

    with open(CLASS_NAMES_SAVE_PATH, "w") as f:
        json.dump(class_names, f, indent=4)
    print(f"\n[OK] Saved {len(class_names)} class names to '{CLASS_NAMES_SAVE_PATH}'")

    # 3. Build CNN Architecture using Keras
    num_classes = len(class_names)
    print(f"\nBuilding CNN model for {num_classes} plant disease classes...")

    base_model = MobileNetV2(
        input_shape=(224, 224, 3),
        include_top=False,
        weights='imagenet'
    )
    base_model.trainable = False

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.3)(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.2)(x)
    outputs = Dense(num_classes, activation='softmax')(x)

    model = Model(inputs=base_model.input, outputs=outputs)

    # Compile with Adam & Categorical Crossentropy
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    # 4. Callbacks: EarlyStopping & ModelCheckpoint
    callbacks = [
        EarlyStopping(
            monitor='val_loss',
            patience=5,
            restore_best_weights=True,
            verbose=1
        ),
        ModelCheckpoint(
            MODEL_SAVE_PATH,
            monitor='val_accuracy',
            save_best_only=True,
            verbose=1
        )
    ]

    # 5. Train Model
    print(f"\nTraining for up to {EPOCHS} epochs...")
    history = model.fit(
        train_generator,
        epochs=EPOCHS,
        validation_data=val_generator,
        callbacks=callbacks
    )

    # 6. Display Metrics & Generate Graphs
    train_acc = history.history.get('accuracy', [])
    val_acc = history.history.get('val_accuracy', [])
    train_loss = history.history.get('loss', [])
    val_loss = history.history.get('val_loss', [])

    print("\n" + "=" * 60)
    print(f"Final Training Accuracy:   {train_acc[-1]*100:.2f}%")
    print(f"Final Validation Accuracy: {val_acc[-1]*100:.2f}%")
    print(f"Final Training Loss:       {train_loss[-1]:.4f}")
    print(f"Final Validation Loss:     {val_loss[-1]:.4f}")
    print("=" * 60)

    # Plot & Save Accuracy and Loss Graphs
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(train_acc, label='Training Accuracy', color='green', linewidth=2)
    plt.plot(val_acc, label='Validation Accuracy', color='blue', linewidth=2)
    plt.title('Training & Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(train_loss, label='Training Loss', color='orange', linewidth=2)
    plt.plot(val_loss, label='Validation Loss', color='red', linewidth=2)
    plt.title('Training & Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(PLOT_SAVE_PATH)
    print(f"\n[OK] Training history graph saved to '{PLOT_SAVE_PATH}'")
    print(f"[SUCCESS] Model saved to '{MODEL_SAVE_PATH}'")

if __name__ == "__main__":
    main()
