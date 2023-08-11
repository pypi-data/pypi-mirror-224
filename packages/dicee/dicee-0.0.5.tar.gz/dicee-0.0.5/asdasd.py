from dicee.executer import Execute
from dicee.config import Namespace

args = Namespace()
args.path_dataset_folder = "KGs/UMLS"
args.trainer = "PL"
args.model = 'Pykeen_DistMult'
args.num_epochs = 10
args.batch_size = 256
args.lr = 0.1
args.num_workers = 1
args.num_core = 1
args.scoring_technique = "KvsAll"
args.num_epochs = 10
Execute(args).start()

exit(1)
from dicee import KGE
"""
Total Runtime: 10.972 seconds
Evaluate DistMult on Train set
Num of triples 5216
** Evaluation without batching
{'H@1': 0.5921203987730062, 'H@3': 0.7906441717791411, 'H@10': 0.9198619631901841, 'MRR': 0.7101174839158373}
Evaluate DistMult of Validation set
Num of triples 652
** Evaluation without batching
{'H@1': 0.5299079754601227, 'H@3': 0.7239263803680982, 'H@10': 0.8742331288343558, 'MRR': 0.6533908333225035}
Evaluate DistMult of Test set
Num of triples 661
** Evaluation without batching
{'H@1': 0.4863842662632375, 'H@3': 0.7193645990922845, 'H@10': 0.8835098335854765, 'MRR': 0.6257917477391873}
Total Runtime: 16.664 seconds

"""
# Distmult trained on UMLS with neg sample
model = KGE(path="Experiments/2023-08-02 20-14-05.287000")
dataset = []
with open("KGs/UMLS/train.txt", "r") as r:
    for i in r.readlines():
        s, p, o = i.split()
        dataset.append((s, p, o))
model.eval_lp_performance(dataset=dataset, filtered=True)

dataset = []
with open("KGs/UMLS/valid.txt", "r") as r:
    for i in r.readlines():
        s, p, o = i.split()
        dataset.append((s, p, o))
model.eval_lp_performance(dataset=dataset, filtered=True)
dataset = []
with open("KGs/UMLS/test.txt", "r") as r:
    for i in r.readlines():
        s, p, o = i.split()
        dataset.append((s, p, o))
model.eval_lp_performance(dataset=dataset, filtered=True)
exit(1)
model.eval_lp_performance(dataset=dataset, filtered=False)

dataset = [("acquired_abnormality", "location_of", "experimental_model_of_disease"),
           ("anatomical_abnormality", "manifestation_of", "physiologic_function"),
           ("alga", "isa", "entity")]
model.eval_lp_performance(dataset=dataset, filtered=True)
model.eval_lp_performance(dataset=dataset, filtered=False)