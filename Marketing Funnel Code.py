
# MARKETING FUNNEL AND CONVERSION PERFORMANCE DASHBOARD
# Leads Dataset — X Education
# -----------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import numpy as np


# LOAD AND PREPARE DATA
# -----------------------------------------------------------

df = pd.read_csv(r'C:\Anaconda3\Marketing Funnel\Leads.csv')

df['TotalVisits']                  = pd.to_numeric(df['TotalVisits'],                  errors='coerce').fillna(0)
df['Page Views Per Visit']         = pd.to_numeric(df['Page Views Per Visit'],          errors='coerce').fillna(0)
df['Total Time Spent on Website']  = pd.to_numeric(df['Total Time Spent on Website'],   errors='coerce').fillna(0)

# Clean Lead Source
df['Lead Source'] = df['Lead Source'].str.strip().str.title()
df['Lead Source'] = df['Lead Source'].replace({'Google': 'Google', 'Bing': 'Bing'})

# Split into 12 equal cohorts by Lead Number 
df_sorted = df.sort_values('Lead Number').reset_index(drop=True)
df_sorted['Cohort'] = pd.cut(
    df_sorted.index, bins=12,
    labels=[f'C{i}' for i in range(1, 13)]
)


# CALCULATE KPIs
# ----------------------------------------------------------------

total_visitors    = int(df['TotalVisits'].sum())
total_leads       = len(df)
total_converted   = int(df['Converted'].sum())
total_not_conv    = total_leads - total_converted
lead_conv_rate    = round(total_converted / total_leads * 100, 2)
visitor_lead_rate = round(total_leads / max(total_visitors, 1) * 100, 2)
dropoff_rate      = round(100 - lead_conv_rate, 2)


# COLOUR THEME
# ------------------------------------------------------------------

bg_color    = '#E8EEF4'
card_color  = '#FFFFFF'
title_color = '#1A3A5C'
dark_blue   = '#2E6DA4'
light_blue  = '#A8C4E0'
text_color  = '#2C3E50'
label_color = '#5D7A96'


# FIGURE AND LAYOUT
# ----------------------------------------------------------------

fig = plt.figure(figsize=(22, 13), facecolor=bg_color)
fig.patch.set_facecolor(bg_color)

fig.text(0.5, 0.97,
         'Marketing Funnel & Conversion Performance Dashboard',
         ha='center', va='top',
         fontsize=22, fontweight='bold', color=title_color)

gs = gridspec.GridSpec(
    3, 3,
    figure=fig,
    top=0.91, bottom=0.06,
    left=0.04, right=0.98,
    hspace=0.45, wspace=0.3,
    height_ratios=[0.18, 0.41, 0.41]
)


# HELPER FUNCTIONS
# ---------------------------------------------------------------

def card(ax):
    ax.set_facecolor(card_color)
    for spine in ax.spines.values():
        spine.set_visible(False)

def style_ax(ax):
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.tick_params(colors=text_color)


# ROW 1 — KPI CARDS
# ----------------------------------------------------------------

kpi_gs = gridspec.GridSpecFromSubplotSpec(
    1, 6, subplot_spec=gs[0, :], wspace=0.04
)

kpis = [
    ('Total\nVisitors',        f'{total_visitors:,}'),
    ('Total\nLeads',           f'{total_leads:,}'),
    ('Total\nCustomers',       f'{total_converted:,}'),
    ('Traffic to \nLead Rate',   f'{visitor_lead_rate:.2f}%'),
    ('Lead to\nCustomer Rate',  f'{lead_conv_rate:.2f}%'),
    ('Drop-off\nRate',         f'{dropoff_rate:.2f}%'),
]

for i, (label, value) in enumerate(kpis):
    ax = fig.add_subplot(kpi_gs[i])
    card(ax)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_xticks([]); ax.set_yticks([])
    ax.text(0.5, 0.78, label,
            ha='center', va='center', fontsize=8.5, color=label_color)
    ax.text(0.5, 0.38, value,
            ha='center', va='center', fontsize=16,
            fontweight='bold', color=title_color)
    ax.axhline(y=0.06, color=dark_blue, linewidth=3, xmin=0.1, xmax=0.9)

# ROW 2 — LEFT: Funnel Chart  Visitors to Leads to Customers
# -----------------------------------------------------------

ax1 = fig.add_subplot(gs[1, 0])
card(ax1)

funnel_stages = ['Total Visitors', 'Total Leads', 'Customers']
funnel_values = [total_visitors, total_leads, total_converted]
funnel_colors = [dark_blue, '#5B9BD5', light_blue]

# Normalize widths 
max_val = funnel_values[0]
widths = [v / max_val for v in funnel_values]

# Vertical positions (top → bottom)
y_pos = list(range(len(funnel_stages)))[::-1]

for i, (stage, val, width, color, y) in enumerate(
        zip(funnel_stages, funnel_values, widths, funnel_colors, y_pos)):

    # Center each bar
    left = (1 - width) / 2

    ax1.barh(y, width, left=left,
             height=0.6, color=color, edgecolor='none')

    # Inside value text
    pct = val / max_val * 100
    ax1.text(0.5, y,
             f'{val:,}',
             ha='center', va='center',
             fontsize=10, fontweight='bold', color='white')

    # LEFT SIDE LABELS (what you asked for)
    ax1.text(left - 0.05, y,
             stage,
             ha='right', va='center',
             fontsize=9, color=text_color)

    # RIGHT SIDE PERCENTAGES
    ax1.text(left + width + 0.05, y,
             f'{pct:.1f}%',
             ha='left', va='center',
             fontsize=9, color=text_color)

# ----- TOP 100% INDICATOR -----
ax1.plot([0, 1], [len(funnel_stages)-0.4]*2, color='gray', lw=1)
ax1.text(0.5, len(funnel_stages)-0.2, '100%',
         ha='center', fontsize=9, color='gray')

# ----- BOTTOM % INDICATOR -----
bottom_width = widths[-1]
left_bottom = (1 - bottom_width) / 2

ax1.plot([left_bottom, left_bottom + bottom_width], [-0.6, -0.6],
         color='gray', lw=1)

ax1.text(0.5, -0.85,
         f'{bottom_width*100:.0f}%',
         ha='center', fontsize=9, color='gray')

# Clean styling
ax1.set_xlim(-0.25, 1.25)
ax1.set_ylim(-1, len(funnel_stages))
ax1.axis('off')

ax1.set_title('Funnel: Visitors → Leads → Customers',
              fontsize=11, fontweight='bold',
              color=title_color, pad=10)

style_ax(ax1)

# ROW 2 — MIDDLE: Conversion by Channel (Lead Source)
# ------------------------------------------------------------------

ax2 = fig.add_subplot(gs[1, 1])
card(ax2)

ch_conv = df.groupby('Lead Source')['Converted'].agg(['sum', 'count'])
ch_conv = ch_conv[ch_conv['count'] >= 10]
ch_conv['rate'] = (ch_conv['sum'] / ch_conv['count'] * 100).round(2)
ch_conv = ch_conv.sort_values('rate', ascending=False).head(6)

bar_colors2 = [dark_blue if i == 0 else light_blue for i in range(len(ch_conv))]
bars2 = ax2.bar(ch_conv.index, ch_conv['rate'].values,
                color=bar_colors2, width=0.45, edgecolor='none')

for bar, val in zip(bars2, ch_conv['rate'].values):
    ax2.text(bar.get_x() + bar.get_width()/2, val + 0.5,
             f'{val:.2f}%', ha='center', va='bottom',
             fontsize=8, fontweight='bold', color=title_color)

ax2.set_ylabel('Conversion Rate (%)', fontsize=8, color=label_color)
ax2.set_xlabel('Channel (Lead Source)', fontsize=8, color=label_color)
ax2.set_title('Conversion by Channel', fontsize=11,
              fontweight='bold', color=title_color, pad=8)
ax2.tick_params(labelsize=7)
plt.setp(ax2.get_xticklabels(), rotation=20, ha='right')
ax2.set_ylim(0, ch_conv['rate'].max() + 18)
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))
style_ax(ax2)


# ROW 2 — RIGHT: Drop-off Analysis (funnel stage losses)
# ------------------------------------------------------------------

ax3 = fig.add_subplot(gs[1, 2])
card(ax3)

engaged      = df[df['Total Time Spent on Website'] > 0].shape[0]
active_pages = df[df['Page Views Per Visit'] > 1].shape[0]
customers    = total_converted

stages     = ['Visited', 'Engaged', 'Browsed\n>1 Page', 'Converted']
stage_vals = [total_leads, engaged, active_pages, customers]
dropoffs   = [stage_vals[i] - stage_vals[i+1] for i in range(len(stage_vals)-1)]
dropoff_pcts = [round(d / stage_vals[i] * 100, 2) for i, d in enumerate(dropoffs)]

colors3 = [dark_blue, '#5B9BD5', light_blue, '#7FB3D3']
bars3 = ax3.bar(stages, stage_vals, color=colors3, width=0.5, edgecolor='none')

for i, (bar, val) in enumerate(zip(bars3, stage_vals)):
    ax3.text(bar.get_x() + bar.get_width()/2, val + 50,
             f'{val:,}', ha='center', va='bottom',
             fontsize=8, fontweight='bold', color=title_color)
    if i < len(dropoffs):
        mid_x = bar.get_x() + bar.get_width() + 0.05
        mid_y = (stage_vals[i] + stage_vals[i+1]) / 2
        ax3.annotate(f'−{dropoff_pcts[i]:.1f}%',
                     xy=(mid_x, mid_y), fontsize=7.5,
                     color='#C0392B', fontweight='bold', va='center')

ax3.set_ylabel('Number of Leads', fontsize=8, color=label_color)
ax3.set_title('Drop-off Analysis by Funnel Stage', fontsize=11,
              fontweight='bold', color=title_color, pad=8)
ax3.tick_params(labelsize=8)
ax3.set_ylim(0, max(stage_vals) + 600)
ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))
style_ax(ax3)


# ROW 3 — LEFT: Conversion Rate Trend by Lead Cohort
# ------------------------------------------------------------------

ax4 = fig.add_subplot(gs[2, 0])
card(ax4)

monthly = df_sorted.groupby('Cohort', observed=True)['Converted'].agg(['sum', 'count'])
monthly['rate'] = (monthly['sum'] / monthly['count'] * 100).round(2)

x_pos = range(len(monthly))
ax4.fill_between(x_pos, monthly['rate'].values,
                 color=light_blue, alpha=0.45)
ax4.plot(x_pos, monthly['rate'].values,
         color=dark_blue, linewidth=2, marker='o',
         markersize=5, markerfacecolor=dark_blue)

for x, val in zip(x_pos, monthly['rate'].values):
    ax4.text(x, val + 0.6, f'{val:.1f}%',
             ha='center', fontsize=7, color=title_color, fontweight='bold')

ax4.set_xticks(list(x_pos))
ax4.set_xticklabels(
    [f'Cohort {i+1}' for i in range(len(monthly))],
    fontsize=6.5, rotation=30, ha='right', color=text_color
)
ax4.set_ylabel('Conversion Rate (%)', fontsize=8, color=label_color)
ax4.set_xlabel('Lead Cohort (grouped by acquisition sequence)', fontsize=7, color=label_color)
ax4.set_title('Conversion Rate Trend by Lead Cohort', fontsize=11,
              fontweight='bold', color=title_color, pad=8)
ax4.set_ylim(0, monthly['rate'].max() + 8)
ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))
style_ax(ax4)


# ROW 3 — MIDDLE: Channel Comparison, Volume vs Quality
# ------------------------------------------------------------------

ax5 = fig.add_subplot(gs[2, 1])
card(ax5)

ch_all = df.groupby('Lead Source')['Converted'].agg(['sum', 'count'])
ch_all = ch_all[ch_all['count'] >= 10].copy()
ch_all['rate'] = (ch_all['sum'] / ch_all['count'] * 100).round(2)
ch_all = ch_all.sort_values('count', ascending=False).head(6)

x5    = np.arange(len(ch_all))
width = 0.35

ax5.bar(x5 - width/2, ch_all['count'].values,
        width=width, color=light_blue, edgecolor='none', label='Volume')

ax5b = ax5.twinx()
ax5b.bar(x5 + width/2, ch_all['rate'].values,
         width=width, color=dark_blue, edgecolor='none', label='Conv. Rate %')

ax5.set_ylabel('Lead Volume', fontsize=8, color=label_color)
ax5b.set_ylabel('Conversion Rate (%)', fontsize=8, color=label_color)
ax5.set_xticks(x5)
ax5.set_xticklabels(ch_all.index.tolist(), fontsize=7, rotation=20, ha='right', color=text_color)
ax5.set_title('Channel: Volume vs Conversion Quality', fontsize=11,
              fontweight='bold', color=title_color, pad=8)
ax5.tick_params(axis='y', colors=text_color, labelsize=7)
ax5b.tick_params(axis='y', colors=text_color, labelsize=7)
ax5.set_ylim(0, ch_all['count'].max() + 500)
ax5b.set_ylim(0, ch_all['rate'].max() + 20)

legend_handles = [
    mpatches.Patch(color=light_blue, label='Volume'),
    mpatches.Patch(color=dark_blue,  label='Conv. Rate %')
]
ax5.legend(handles=legend_handles, loc='upper right', fontsize=7.5, frameon=False)

for spine in ['top']:
    ax5.spines[spine].set_visible(False)
    ax5b.spines[spine].set_visible(False)
ax5.spines['left'].set_color('#CCCCCC')
ax5.spines['bottom'].set_color('#CCCCCC')
ax5b.spines['right'].set_color('#CCCCCC')


# ROW 3 — RIGHT: Conversion Rate by Specialization
# -------------------------------------------------------------------

ax6 = fig.add_subplot(gs[2, 2])
card(ax6)

spec_conv = df.groupby('Specialization')['Converted'].agg(['sum', 'count'])
spec_conv = spec_conv[spec_conv['count'] >= 30].copy()
spec_conv['rate'] = (spec_conv['sum'] / spec_conv['count'] * 100).round(2)
spec_conv = spec_conv.sort_values('rate', ascending=True).tail(7)

# Shorten long names
name_map = {
    'Banking, Investment And Insurance' : 'Banking & Insurance',
    'Healthcare Management'             : 'Healthcare Mgmt',
    'Marketing Management'              : 'Marketing Mgmt',
    'Operations Management'             : 'Operations Mgmt',
    'Human Resource Management'         : 'HR Management',
    'Finance Management'                : 'Finance Mgmt',
    'Business Administration'           : 'Business Admin',
    'Supply Chain Management'           : 'Supply Chain',
    'IT Projects Management'            : 'IT Projects',
    'Media and Advertising'             : 'Media & Advert.',
}
spec_conv.index = [name_map.get(i, i) for i in spec_conv.index]

bar_colors6 = [dark_blue if i == len(spec_conv) - 1 else light_blue
               for i in range(len(spec_conv))]

bars6 = ax6.barh(spec_conv.index, spec_conv['rate'].values,
                 color=bar_colors6, height=0.5, edgecolor='none')

for bar, val in zip(bars6, spec_conv['rate'].values):
    ax6.text(val + 0.4,
             bar.get_y() + bar.get_height()/2,
             f'{val:.2f}%',
             va='center', fontsize=8,
             fontweight='bold', color=title_color)

ax6.set_xlabel('Conversion Rate (%)', fontsize=8, color=label_color)
ax6.set_title('Conversion Rate by Specialization', fontsize=11,
              fontweight='bold', color=title_color, pad=8)
ax6.tick_params(labelsize=8)
ax6.set_xlim(0, spec_conv['rate'].max() + 15)
ax6.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))
style_ax(ax6)


# SAVE AND SHOW
# ----------------------------------------------------------------------

plt.savefig(
    r'C:\Anaconda3\Marketing Funnel\Funnel_Dashboard.pdf',
    dpi=150, bbox_inches='tight',
    facecolor=bg_color
)

plt.show()