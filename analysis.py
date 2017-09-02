def make_barplot(national_data, local_data, county, features, ax):
    loc_data = local_data.loc[local_data['county'] == county]
    
    race = [f.split('_')[1] for f in features]
    race_qualifiers = [f.split('_')[2] for f in features]
    compare_races = []
    compare_qualifiers = []
    for f in features:
        split = f.split('_')
        if len(split) == 6:
            compare_races.append(split[4])
            compare_qualifiers.append(split[5])
        elif len(split) == 5:
            compare_races.append(split[1])
            compare_qualifiers.append(split[-1])
        else:
            raise ValueError
    assert all(compare_races[0] == cr for cr in compare_races)
    assert all(compare_qualifiers[0] == cq for cq in compare_qualifiers)
    compare_race = compare_races[0]
    compare_qualifier = compare_qualifiers[0]
    
    labels = []
    for r, q in zip(race, race_qualifiers):
        labels.append('National:\n{} {}'.format(r, q))
        labels.append('{}:\n{} {}'.format(county, r, q))
    
    n_bars = 2 * len(features)
    ycur = 0
    y = []
    for ii in range(len(features)):
        y.append(ycur)
        ycur += 1
        y.append(ycur)
        ycur += 1.5
    
    x = []
    for f in features:
        x.append(national_data[f].values[0])
        x.append(loc_data[f].values[0])
    
    y = y[::-1]
    labels = labels
    
    ax.barh(y, x)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    
    ax.set_xlabel('Relative risk of being shot by police vs. {} {}'.format(compare_race, compare_qualifier))
    ax.axvline(1, linestyle='--', lw=2, c='k')
