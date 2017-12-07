from ssd.ssdmodel import SSDModel
from trainer.trainer import Trainer
from trainer.preparedata import PrepareData
from trainer.postprocessingdata import PostProcessingData
from trainer import train_params
from experiments import ssd512_voc0712 as sv
from experiments import finetune_person as fp

if __name__ == '__main__':
    params = fp.step3_1

    feature_extractor = params.feature_extractor
    model_name = params.model_name
    weight_decay = params.weight_decay
    batch_size = params.batch_size
    labels_offset = params.labels_offset
    matched_thresholds = params.matched_thresholds

    ssd_model = SSDModel(feature_extractor, model_name, weight_decay)
    data_preparer = PrepareData(ssd_model, batch_size, labels_offset, matched_thresholds)
    data_postprocessor = PostProcessingData(ssd_model)
    ssd_trainer = Trainer(ssd_model, data_preparer, data_postprocessor, params)

    ssd_trainer.start_training()
