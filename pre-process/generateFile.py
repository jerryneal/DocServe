import random, string, sys, os, errno, math


# Rules
# Number of files per folder = 23
# lines = 10000 #Number of lines
files_per_folder = 23
lines_per_file = 30


def organizeStructure(lines):
    '''

    :return:
    mockData = { '1_30':['1_10.txt','11_20.txt','21_30.txt'],
                 '31_60':['31_40.txt','41_50.txt','51_60.txt'] }
    '''
    # lines = 10000  # Number of lines
    files_per_folder = 30
    lines_per_file = 30

    paths = []

    # Get file and folder numbers
    files = int(math.ceil(float(lines) / float(lines_per_file)))
    folders = 1 if files < files_per_folder else int(files % files_per_folder)
    # print 'Folders : %s' % folders

    # Create folders for one or less
    if folders <= 1:

        start = 1
        for i in range(files):
            end = start + lines_per_file
            name = '%s_%s.txt' % (start, end)
            start = end + 1
            paths.append('1_%s/%s' % (lines, name))

    else:
        lines_counter = 0
        while lines_counter < lines:

            start_fold_name = 1
            for i in range(1, folders):
                # print i
                end_fold_name = start_fold_name + (math.ceil(float(lines) / float(folders)))
                name = '%s_%s' % (int(start_fold_name), int(end_fold_name))
                start_fold_name = end_fold_name
                lines_counter += end_fold_name
                paths.append(name)

            if (lines - lines_counter) < (math.ceil(float(lines) / float(folders))):
                name = '%s_%s' % (int(start_fold_name), int(lines))
                paths.append(name)

    # Make paths for bigger folders
    final_paths = []
    start = 1

    for folder in paths:

        for j in range(files_per_folder):
            line_counter = 0
            end = start + lines_per_file
            name = '%s_%s.txt' % (start, end)
            start = end
            line_counter += end
            final_paths.append('%s/%s' % (folder, name))

            # print folder
            # print int(folder.split('_')[1])
            # print lines_counter
            # print lines_per_file



            if (int(folder.split('_')[1]) - line_counter) < lines_per_file:
                name = '%s_%s' % (int(start), folder.split('_')[1])
                final_paths.append(name)

    print len(final_paths)

    for name in final_paths:

        # print name
        dir_name = '../mockData/%s' % str(name)

        if not os.path.exists(os.path.dirname(dir_name)):
            try:
                os.makedirs(os.path.dirname(dir_name))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open("../mockData/{}".format(name), "w+") as f:
            rep = name.rsplit('.')[0].split('/')[1].split('_')
            start_line = rep[0]
            end_line = rep[1]
            print 'name:',name
            print 'start_line:', start_line
            print 'end_line:',end_line
            range1 = lambda s, e: range(int(s), int(e))
            good_quotes = [
                'There is nothing permanent except change',
                'Gratitude can transform common days into thanksgivings, turn routine jobs into joy, and change ordinary opportunities into blessings',
                'In the sweetness of friendship let there be laughter, and sharing of pleasures. For in the dew of little things the heart finds its morning and is refreshed',
                'Moral indignation is jealousy with a halo.',
                'Glory is fleeting, but obscurity is forever.',
                'Victory goes to the player who makes the next-to-last mistake.',
                'Dont be so humble - you are not that great.',
                'His ignorance is encyclopedic',
                'If a man does his best, what else is there',
                'Political correctness is tyranny with manners',
                'You can avoid reality, but you cannot avoid the consequences of avoiding reality',
                'People demand freedom of speech to make up for the freedom of thought which they avoid',
                'Not everything that can be counted counts, and not everything that counts can be counted',
                'A lie gets halfway around the world before the truth has a chance to get its pants on'

            ]
            for i in range1(start_line, end_line):
                f.write('%s. %s. \n' % (i, random.choice(good_quotes)))


def makeSubFiles(file):
    '''
    Split file into folders and subfiles
    :param file:
    :return: return a directory of subfolders with files in them
    '''

    lengthOfFile = os.system('wc - l < %s' % file)

    with open(file,'rb') as f: # buffering=1024, the default is already optimized for this CPU
        pass




if __name__ == '__main__':
    num = int(sys.argv[1])
    if num is not None:
        # generatefile(lines=num)
        organizeStructure(num)
    else:
        print 'Files/Folders not created'
