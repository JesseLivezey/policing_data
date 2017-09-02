def make_barplot(national_data, local_data, county, features, ax):
    height = .8
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
        labels.append('County')
        labels.append('{} {}'.format(r, q))
        labels.append('National')
    
    n_bars = 2 * len(features)
    ycur = 0
    y = []
    y_labels = []
    for ii in range(len(features)):
        y.append(ycur)
        y_labels.append(ycur)
        y_labels.append(ycur + .5)
        ycur += 1
        y.append(ycur)
        y_labels.append(ycur)
        ycur += 1.5
    
    x = []
    for f in features:
        x.append(national_data[f].values[0])
        x.append(loc_data[f].values[0])
    
    y = y[::-1]
    labels = labels
    
    baseline_mid = .5 * (y[0] + y[-1])
    baseline_height = abs((y[-1] - y[0])) + 2 * height
    ax.barh(baseline_mid, 1, height=baseline_height, color='gray', alpha=.8)
    
    ax.barh(y, x, height=height, alpha=.8)
    ax.set_yticks(y_labels)
    ax.set_yticklabels(labels)
    ax.set_xticks([])
    
    ax.set_xlabel('Relative risk of being shot by police\nvs. {} {}'.format(compare_race, compare_qualifier))
    #ax.axvline(1, linestyle='--', lw=2, c='k')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_ylim(baseline_mid - .5 * baseline_height, baseline_mid + .5 * baseline_height)
    ax.set_title(county)
