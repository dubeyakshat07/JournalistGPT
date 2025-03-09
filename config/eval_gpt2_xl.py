# evaluate the base gpt2
# n_layer=48, n_head=25, n_embd=1600
# 1558M parameters
batch_size = 8
eval_iters = 500 # use more iterations to get good estimate
eval_only = True
wandb_log = False
init_from = 'gpt2-xl'

# on macbook also add
device = 'mps'  # run on cpu only
compile = False # do not torch compile the model