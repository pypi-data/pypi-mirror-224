import torch
import dicee
from dicee import DistMult
import polars as pl
import time

print("Reading KG...", end=" ")
start_time = time.time()
df = pl.read_parquet("dbpedia-2022-12-nt.parquet.snappy")
print(f"took {time.time() - start_time}")
print("Unique entities...", end=" ")
start_time = time.time()
unique_entities = pl.concat((df.get_column('subject'), df.get_column('object'))).unique().rename('entity').to_list()
print(f"took {time.time() - start_time}")

print("Unique relations...", end=" ")
start_time = time.time()
unique_relations = df.unique(subset=["relation"]).select("relation").to_series().to_list()
print(f"took {time.time() - start_time}")

print("Entity index mapping...", end=" ")
start_time = time.time()
entity_to_idx = {ent: idx for idx, ent in enumerate(unique_entities)}

print("Relation index mapping...", end=" ")
start_time = time.time()
rel_to_idx = {rel: idx for idx, rel in enumerate(unique_relations)}
print(f"took {time.time() - start_time}")

print("Constructing training data...", end=" ")
start_time = time.time()
train_data = df.with_columns(pl.col("subject").map_dict(entity_to_idx).alias("subject"),
                             pl.col("relation").map_dict(rel_to_idx).alias("relation"),
                             pl.col("object").map_dict(entity_to_idx).alias("object")).to_numpy()
print(f"took {time.time() - start_time}")
print("Deleting dataframe...", end=" ")
del df

print("KGE model...", end=" ")
start_time = time.time()
model = DistMult(args={"num_entities": len(entity_to_idx), "num_relations": len(rel_to_idx), "embedding_dim": 10})
print(f"took {time.time() - start_time}", end=" ")
print("Optimizer...")
start_time = time.time()
optimizer = model.configure_optimizers()

model.cuda()

loss_function = model.loss_function

batch_size = 32
start_index = 0
print("Training...")
