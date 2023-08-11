from dicee.executer import Execute
from dicee.config import Namespace
args = Namespace()
args.path_dataset_folder = "KGs/UMLS"
args.trainer = "PL"
args.model = 'Pykeen_TransE'
args.num_epochs = 10
args.batch_size = 256
args.lr = 0.1
args.num_workers = 1
args.num_core = 1
args.scoring_technique = "KvsAll"
args.num_epochs = 10
args.sample_triples_ratio = None
args.read_only_few = None
args.num_folds_for_cv = None
Execute(args).start()
