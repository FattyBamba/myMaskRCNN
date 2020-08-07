history = self.keras_model.fit_generator(
            train_generator,
            initial_epoch=self.epoch,
            epochs=epochs,
            steps_per_epoch=self.config.STEPS_PER_EPOCH,
            callbacks=callbacks,
            validation_data=val_generator,
            validation_steps=self.config.VALIDATION_STEPS,
            max_queue_size=100,
            workers=1,                  # was workers
            use_multiprocessing=False,  # was True
            verbose=self.config.TRAINING_VERBOSE
        )
        self.epoch = max(self.epoch, epochs)
        return history