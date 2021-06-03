import optparse, csv

keyColumn = 1
sortColumns = [2, -2]


# ------------------------------------------------------------------------------

def parseArgs():
    parser = optparse.OptionParser(description='Extract hyde scores',
                                   usage="usage: %prog [options] csv-hyde-scores-file")
    parser.add_option('--nofposes', type='int', help='default: all', default=-1)
    parser.add_option('--test', action='store_true', help=optparse.SUPPRESS_HELP)
    parser.add_option('--oneline', help='compressed output, one line per ligand', action='store_true')

    options, args = parser.parse_args()
    if len(args) != 1 and not options.test:
        parser.error("Missing csv-hyde-scores-file")

    if not options.test:
        options.csv_hyde_scores_file = args[0]

    return options


# ------------------------------------------------------------------------------

def run(nofPoses, csvFile):
    r"""
    >>> import StringIO
    >>> run(-1, StringIO.StringIO('''\
    ... #receptor;ligand;HYDE;LE;dGSat;dGDesol;LigLipo;LigHydr;RecLipo;RecHydr;OptScore;dGExp;RMSH;SIMIxH;RMSnoH;SIMIxnoH;Error;LigESat;LigEDes;RecESat;RecEDes;Plgp<=-1;Plgp<0;NrLgESat;Inter;Intra;Tors;ExpRec;HYDE_MAX;TS1Score;
    ... "1stp";"1stp_001";-52.033;3.252;-80.496;28.462;-14.302;33.388;-22.519;31.896;-118.096;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-39.064;19.086;-41.431;9.377;3;5;5;-48.622;-10.995;8.118;0.000;-52.033;-52.921;
    ... "1stp";"1stp_001";-52.538;3.284;-80.496;27.958;-14.533;33.388;-22.667;31.770;-116.357;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-39.064;18.855;-41.431;9.103;3;5;5;-27.429;-9.759;23.483;0.000;-52.538;-53.299;
    ... "1stp";"1stp_002";-52.746;3.297;-80.277;27.530;-13.986;33.396;-22.672;30.792;-114.466;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-39.064;19.410;-41.212;8.120;3;5;5;-20.845;-5.141;22.659;0.000;-52.746;-52.713;
    ... "1stp";"1stp_003";-43.552;2.722;-73.834;30.282;-13.532;34.257;-22.649;32.206;-93.687;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-36.201;20.725;-37.633;9.557;3;5;5;18.234;-8.319;14.390;0.000;-49.246;-50.948;
    ... "1stp";"1stp_004";-52.266;3.267;-80.706;28.440;-14.580;33.388;-22.150;31.782;-117.811;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-39.064;18.808;-41.642;9.632;3;5;5;-43.590;-10.310;6.306;0.000;-52.266;-52.871;
    ... "1stp";"1stp_005";-50.501;3.156;-79.759;29.259;-14.225;34.256;-23.165;32.392;-114.124;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-38.751;20.031;-41.008;9.227;3;5;5;-37.732;-10.291;13.755;0.000;-54.223;-53.342;
    ... "1stp";"1stp_006";-51.751;3.234;-80.489;28.738;-13.959;33.388;-22.933;32.242;-115.809;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-39.062;19.429;-41.427;9.309;3;5;5;-54.512;-10.998;11.179;0.000;-51.755;-52.990;
    ... "1stp";"1stp_007";-46.675;2.917;-76.209;29.534;-14.329;33.388;-22.069;32.543;-98.886;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-37.223;19.060;-38.986;10.474;3;5;5;22.051;-8.898;16.024;0.000;-50.029;-51.640;
    ... "1stp";"1stp_008";-44.289;2.768;-74.694;30.406;-13.373;34.256;-22.072;31.594;-91.676;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-37.012;20.883;-37.683;9.523;3;5;5;-7.176;-8.853;17.598;0.000;-51.284;-50.384;
    ... "1stp";"1stp_009";-51.774;3.236;-80.496;28.722;-13.501;33.388;-21.578;30.413;-115.834;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-39.064;19.887;-41.431;8.835;3;5;5;-57.280;-10.104;7.217;0.000;-51.774;-51.179;
    ... '''))
    (['receptor', 'ligand', 'HYDE', 'LE', 'dGSat', 'dGDesol', 'LigLipo', 'LigHydr', 'RecLipo', 'RecHydr', 'OptScore', 'dGExp', 'RMSH', 'SIMIxH', 'RMSnoH', 'SIMIxnoH', 'Error', 'LigESat', 'LigEDes', 'RecESat', 'RecEDes', 'Plgp<=-1', 'Plgp<0', 'NrLgESat', 'Inter', 'Intra', 'Tors', 'ExpRec', 'HYDE_MAX', 'TS1Score', ''], {'1stp': {2: ('-52.746', '1stp_002', 4), -2: ('-53.342', '1stp_005', 7)}}, {})
    >>> columnTitles, highScores, errorScores = _
    >>> printResults(columnTitles, highScores, errorScores, -1, False)
    <BLANKLINE>
    Best scores, regarding ** all ** pose(s) per ligand
    <BLANKLINE>
    Ligand 1stp
    ===========
    <BLANKLINE>
               HYDE: -52.746 (1stp_002, line 4)
           TS1Score: -53.342 (1stp_005, line 7)
    <BLANKLINE>
    <BLANKLINE>
    >>> # Test for --oneline
    >>> printResults(columnTitles, highScores, errorScores, -1, True)
    <BLANKLINE>
    Best scores, regarding ** all ** pose(s) per ligand
    <BLANKLINE>
    #Ligand;Error[;;ColumnTitle;BestScore;PoseName;Line]*
    1stp;;;HYDE;-52.746;1stp_002;4;;TS1Score;-53.342;1stp_005;7
    >>> # Test for --nofposes 3
    >>> run(3, StringIO.StringIO('''\
    ... #receptor;ligand;HYDE;LE;dGSat;dGDesol;LigLipo;LigHydr;RecLipo;RecHydr;OptScore;dGExp;RMSH;SIMIxH;RMSnoH;SIMIxnoH;Error;LigESat;LigEDes;RecESat;RecEDes;Plgp<=-1;Plgp<0;NrLgESat;Inter;Intra;Tors;ExpRec;HYDE_MAX;TS1Score;
    ... "1stp";"1stp_001";-52.033;3.252;-80.496;28.462;-14.302;33.388;-22.519;31.896;-118.096;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-39.064;19.086;-41.431;9.377;3;5;5;-48.622;-10.995;8.118;0.000;-52.033;-52.921;
    ... "1stp";"1stp_001";-52.538;3.284;-80.496;27.958;-14.533;33.388;-22.667;31.770;-116.357;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-39.064;18.855;-41.431;9.103;3;5;5;-27.429;-9.759;23.483;0.000;-52.538;-53.299;
    ... "1stp";"1stp_002";-52.746;3.297;-80.277;27.530;-13.986;33.396;-22.672;30.792;-114.466;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-39.064;19.410;-41.212;8.120;3;5;5;-20.845;-5.141;22.659;0.000;-52.746;-52.713;
    ... "1stp";"1stp_003";-43.552;2.722;-73.834;30.282;-13.532;34.257;-22.649;32.206;-93.687;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-36.201;20.725;-37.633;9.557;3;5;5;18.234;-8.319;14.390;0.000;-49.246;-50.948;
    ... "1stp";"1stp_004";-52.266;3.267;-80.706;28.440;-14.580;33.388;-22.150;31.782;-117.811;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-39.064;18.808;-41.642;9.632;3;5;5;-43.590;-10.310;6.306;0.000;-52.266;-52.871;
    ... "1stp";"1stp_005";-50.501;3.156;-79.759;29.259;-14.225;34.256;-23.165;32.392;-114.124;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-38.751;20.031;-41.008;9.227;3;5;5;-37.732;-10.291;13.755;0.000;-54.223;-53.342;
    ... "1stp";"1stp_006";-51.751;3.234;-80.489;28.738;-13.959;33.388;-22.933;32.242;-115.809;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-39.062;19.429;-41.427;9.309;3;5;5;-54.512;-10.998;11.179;0.000;-51.755;-52.990;
    ... "1stp";"1stp_007";-46.675;2.917;-76.209;29.534;-14.329;33.388;-22.069;32.543;-98.886;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-37.223;19.060;-38.986;10.474;3;5;5;22.051;-8.898;16.024;0.000;-50.029;-51.640;
    ... "1stp";"1stp_008";-44.289;2.768;-74.694;30.406;-13.373;34.256;-22.072;31.594;-91.676;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-37.012;20.883;-37.683;9.523;3;5;5;-7.176;-8.853;17.598;0.000;-51.284;-50.384;
    ... "1stp";"1stp_009";-51.774;3.236;-80.496;28.722;-13.501;33.388;-21.578;30.413;-115.834;0.000;1.#IO;1.#IO;1.#IO;1.#IO;0;-39.064;19.887;-41.431;8.835;3;5;5;-57.280;-10.104;7.217;0.000;-51.774;-51.179;
    ... '''))
    (['receptor', 'ligand', 'HYDE', 'LE', 'dGSat', 'dGDesol', 'LigLipo', 'LigHydr', 'RecLipo', 'RecHydr', 'OptScore', 'dGExp', 'RMSH', 'SIMIxH', 'RMSnoH', 'SIMIxnoH', 'Error', 'LigESat', 'LigEDes', 'RecESat', 'RecEDes', 'Plgp<=-1', 'Plgp<0', 'NrLgESat', 'Inter', 'Intra', 'Tors', 'ExpRec', 'HYDE_MAX', 'TS1Score', ''], {'1stp': {2: ('-52.746', '1stp_002', 4), -2: ('-53.299', '1stp_001', 3)}}, {})
    >>> run(-1, StringIO.StringIO('''\
    ... #receptor;ligand;HYDE;LE;dGSat;dGDesol;LigLipo;LigHydr;RecLipo;RecHydr;OptScore;dGExp;RMSH;SIMIxH;RMSnoH;SIMIxnoH;Error;LigESat;LigEDes;RecESat;RecEDes;Plgp<=-1;Plgp<0;NrLgESat;Inter;Intra;Tors;ExpRec;HYDE_MAX;TS1Score;
    ... "1stp";"mtx";-;-;-;-;-;-;-;-;-;-;-;-;-;-;4;-;-;-;-;0;0;0;-;-;-;-;-;-;
    ... '''))
    (['receptor', 'ligand', 'HYDE', 'LE', 'dGSat', 'dGDesol', 'LigLipo', 'LigHydr', 'RecLipo', 'RecHydr', 'OptScore', 'dGExp', 'RMSH', 'SIMIxH', 'RMSnoH', 'SIMIxnoH', 'Error', 'LigESat', 'LigEDes', 'RecESat', 'RecEDes', 'Plgp<=-1', 'Plgp<0', 'NrLgESat', 'Inter', 'Intra', 'Tors', 'ExpRec', 'HYDE_MAX', 'TS1Score', ''], {'mtx': {2: ('0.0', 'mtx', 2), -2: ('0.0', 'mtx', 2)}}, {'mtx': 2})
    """
    highScores = {}
    errorScores = {}
    keyCounts = {}
    lineNumber = 0

    scoresCsv = csv.reader(csvFile, delimiter=';', quotechar='"')
    for fields in scoresCsv:
        lineNumber += 1
        if fields[0][0] == '#':
            fields[0] = fields[0][1:]
            columnTitles = fields
            continue
        keyField = fields[keyColumn]
        key = keyField.rsplit('_', 1)[0]
        if nofPoses > 0:
            keyCounts[key] = keyCounts.get(key, 0) + 1
            if keyCounts[key] > nofPoses:
                continue

        # Check scores
        if not highScores.has_key(key):
            highScores[key] = {}
            for col in sortColumns:
                try:
                    # Test, whether field is a float
                    float(fields[col])
                    highScores[key][col] = (fields[col], keyField, lineNumber)
                except ValueError:
                    if not errorScores.has_key(key):
                        errorScores[key] = lineNumber
                    highScores[key][col] = ("0.0", keyField, lineNumber)
        else:
            for col in sortColumns:
                value = float(fields[col])
                if value < float(highScores[key][col][0]):
                    highScores[key][col] = (fields[col], keyField, lineNumber)

    return columnTitles, highScores, errorScores


# ------------------------------------------------------------------------------

def printResults(columnTitles, highScores, errorScores, nofposes, oneline):
    if nofposes > 0:
        nofPoses = str(nofposes)
    else:
        nofPoses = "all"

    print
    print "Best scores, regarding ** %s ** pose(s) per ligand" % nofPoses
    print
    if oneline:
        print "#Ligand;Error[;;ColumnTitle;BestScore;PoseName;Line]*"
    for key, info in highScores.items():
        if oneline:
            if key in errorScores:
                error = "!! WARNING !! Hyde error output detected in line %d" % errorScores[key]
            else:
                error = ""
            s = "%s;%s" % (key, error)
            for col, colInfo in info.items():
                s += ";;%s;%s;%s;%d" % (columnTitles[col], colInfo[0], colInfo[1], colInfo[2])
            print s
        else:
            s = "Ligand %s" % key
            if key in errorScores:
                s += "  !! WARNING !! Hyde error output detected in line %d" % errorScores[key]
            print "%s\n%s\n" % (s, "=" * len(s))
            for col, colInfo in info.items():
                print "%15s: %s (%s, line %d)" % (
                        columnTitles[col], colInfo[0], colInfo[1], colInfo[2])
            print "\n"



# ------------------------------------------------------------------------------

if __name__ == '__main__':
    args = parseArgs()
    if args.test:
        import sys, doctest
        doctest.testmod()
        sys.exit(0)

    columnTitles, highScores, errorScores = run(args.nofposes, open(args.csv_hyde_scores_file))
    printResults(columnTitles, highScores, errorScores, args.nofposes, args.oneline)
