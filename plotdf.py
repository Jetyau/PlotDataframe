import pandas as pd
import argparse
from glob import glob
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path',default='',type=str, help='dir for logs')
    args = parser.parse_args()

    fig, axs = plt.subplots(2, 2, figsize=(20,20))




    path = args.path
    csv_files = glob(path + './*.csv')
    print(csv_files)
    if csv_files is not []:
        for csv_file in csv_files:
            log = pd.read_csv(csv_file)
            epoch = list(log['epoch'])
            loss = list(log['loss'])
            dice = list(log['dice'])
            val_loss = list(log['val_loss'])
            val_dice = list(log['val_dice'])
            axs[0,0].plot(epoch, loss, label=csv_file)
            axs[0,0].set_title('epoch, train loss')
            axs[0,0].legend(loc="upper right")

            axs[0,1].plot(epoch, val_loss, label=csv_file)
            axs[0,1].set_title('epoch, val_loss')
            axs[0,1].legend(loc="upper right")
            
            axs[1,0].plot(epoch, dice, label=csv_file)
            axs[1,0].set_title('epoch, dice')
            axs[1,0].legend(loc="upper right")

            axs[1,1].plot(epoch, val_dice, label=csv_file)
            axs[1,1].set_title('epoch, val_dice')
            axs[1,1].legend(loc="upper right")





    fig.savefig('./tmp.png')
            





if __name__=="__main__":
    main()