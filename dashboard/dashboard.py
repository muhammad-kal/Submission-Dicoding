import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.ticker as ticker

sns.set(style='dark')

def create_tren_by_season(df):
    tren_by_season = df.groupby(by='season')['cnt'].sum().reset_index()
    tren_by_season['season'] = tren_by_season['season'].replace({1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'})

    return tren_by_season

def create_tren_by_season_2011(df):
    tren_by_season_2011 = df[df['yr'] == 0].groupby(by='season')['cnt'].sum().reset_index()
    tren_by_season_2011['season'] = tren_by_season_2011['season'].replace({1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'})
    return tren_by_season_2011

def create_tren_by_season_2012(df):
    tren_by_season_2012 = df[df['yr'] == 1].groupby(by='season')['cnt'].sum().reset_index()
    tren_by_season_2012['season'] = tren_by_season_2012['season'].replace({1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'})
    return tren_by_season_2012

def create_tren_by_season_total(df):
    tren_by_season_total = df.groupby(by='season')['cnt'].sum().reset_index()
    tren_by_season_total['season'] = tren_by_season_total['season'].replace({1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'})
    return tren_by_season_total
def create_tren_by_season_2011_2012(df):
    peminjaman_tiap_jam_2011_2012 = df.groupby(by=['hr', 'time_of_day']).cnt.sum().reset_index()

    return peminjaman_tiap_jam_2011_2012

def create_peminjaman_tiap_jam_2011_2012(df):
    peminjaman_tiap_jam_2011_2012 = df.groupby(by=['hr', 'time_of_day']).cnt.sum().reset_index()

    return peminjaman_tiap_jam_2011_2012

def create_peminjaman_tiap_jam_2011(df):
    peminjaman_tiap_jam_2011 = df[df['yr'] == 0].groupby(by=['hr', 'time_of_day']).cnt.sum().reset_index()

    return peminjaman_tiap_jam_2011

def create_peminjaman_tiap_jam_2012(df):
    peminjaman_tiap_jam_2012 = df[df['yr'] == 1].groupby(by=['hr', 'time_of_day']).cnt.sum().reset_index()

    return peminjaman_tiap_jam_2012

def create_peminjaman_tiap_jam(df):
    peminjaman_tiap_jam = df.groupby(by=['hr', 'time_of_day'])['cnt'].sum().reset_index()
    return peminjaman_tiap_jam


df_day = pd.read_csv('df_day_modified.csv')
df_hour = pd.read_csv('df_hour_modified.csv')
 
with st.sidebar:
    st.image("logo.png")
    
    year_selected = st.sidebar.selectbox("Pilih Rentang Penyewaan", ['2011', '2012', '2011-2012'])


    #filter berdasarkan tahun
    if year_selected == '2011':
        selected_df = df_hour[df_hour['yr'] == 0]
        st.write('### Data Penyewaan Sepeda 2011')
        st.write(df_hour[df_hour['yr'] == 0])
    elif year_selected == '2012':
        selected_df = df_hour[df_hour['yr'] == 1]
        st.write('### Data Penyewaan Sepeda 2012')
        st.write(df_hour[df_hour['yr'] == 1])
    else : 
        selected_df = df_hour
        st.write('### Data Penyewaan Sepeda 2011-2012')
        st.write(df_hour)
    

    #membagi layar menjadi dua kolom
col1, col2 = st.columns([4,5])

    #kolom 1 : menampilkan visualisasi data

with col1:
    # Visualisasi Data
    st.subheader('Visualisasi Data 📅')
    st.write(' Tren Penyewaan Sepeda Berdasarkan Musim ☁️')
    # Memilih dataset berdasarkan tahun yang dipilih
    if year_selected == '2011':
        tren_by_season = create_tren_by_season_2011(selected_df)
        title = "Total Peminjaman Sepeda Berdasarkan Musim (2011)"
    elif year_selected == '2012':
        tren_by_season = create_tren_by_season_2012(selected_df)
        title = "Total Peminjaman Sepeda Berdasarkan Musim (2012)"
    else:  # Jika memilih '2011-2012'
        tren_by_season = create_tren_by_season_total(selected_df)
        title = "Total Peminjaman Sepeda Berdasarkan Musim (2011-2012)"

    # Plot grafik
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=tren_by_season, x="season", y="cnt", palette="Set2", ax=ax)
    
    ax.set_title(title, fontsize=16, fontweight="bold")
    ax.set_xlabel("Musim", fontsize=12)
    ax.set_ylabel("Total Peminjaman", fontsize=12)
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    # Menampilkan nilai di atas batang
    for i, value in enumerate(tren_by_season['cnt']):
        ax.text(i, value + 5000, f"{value:,}", ha="center", fontsize=12, fontweight="bold")

    st.pyplot(fig)

    #Visualisasi Data
    # Memilih data sesuai tahun yang dipilih
    if year_selected == '2011':
        peminjaman_tiap_jam = create_peminjaman_tiap_jam_2011(df_hour)
        title = "Jumlah Peminjaman Sepeda Berdasarkan Waktu (2011)"
        value_threshold = 30_000
    elif year_selected == '2012':
        peminjaman_tiap_jam = create_peminjaman_tiap_jam_2012(df_hour)
        title = "Jumlah Peminjaman Sepeda Berdasarkan Waktu (2012)"
        value_threshold = 50_000
    else:
        peminjaman_tiap_jam = create_peminjaman_tiap_jam_2011_2012(df_hour)
        title = "Jumlah Peminjaman Sepeda Berdasarkan Waktu (2011-2012)"
        value_threshold = 75_000


    # Visualisasi Data di Streamlit
st.write('Peminjaman Sepeda Berdasarkan Jam ⏰')

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='hr', y='cnt', hue='time_of_day', data=peminjaman_tiap_jam, palette='Set2', errorbar=None, ax=ax)

ax.set_title(title, fontsize=16, fontweight="bold")
ax.set_xlabel("Jam", fontsize=12)
ax.set_ylabel("Total Peminjaman Sepeda", fontsize=12)
ax.grid(axis="y", linestyle="--", alpha=0.7)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)

ax.legend(title="Kategori Waktu")

# Menampilkan nilai di atas batang
for index, row in peminjaman_tiap_jam.iterrows():
    if row["cnt"] > value_threshold:
        ax.text(row["hr"], row["cnt"] * 0.5, f"{row['cnt']:,}", ha="center", fontsize=10, fontweight="bold", color="white", rotation=90)

st.pyplot(fig)


#kolom 2 : menampilkan metrik data
with col2  :
    st.write('##### Metrik Penyewaan Sepeda Tahun ', year_selected,'📊')
    st.metric("Total Penyewaan", selected_df["cnt"].sum())
    st.metric("Registered Users", selected_df["registered"].sum())
    st.metric("Casual Users", selected_df["casual"].sum())


col1, col2 = st.columns([4,5])
with col1 :
    # Memilih data sesuai tahun yang dipilih
    if year_selected == '2011':
        peminjaman_tiap_jam = create_peminjaman_tiap_jam_2011(df_hour)
    elif year_selected == '2012':
        peminjaman_tiap_jam = create_peminjaman_tiap_jam_2012(df_hour)
    else:
        peminjaman_tiap_jam = create_peminjaman_tiap_jam_2011_2012(df_hour)

    filtered_df_sorted = peminjaman_tiap_jam.sort_values(by="cnt", ascending=False)
    st.write("🏆 Top Penyewaan Sepeda Berdasarkan Jam")

    st.dataframe(
        filtered_df_sorted,
        column_order=("hr", "cnt"),
        hide_index=True,
        width=None,
        column_config={
            "hr": st.column_config.TextColumn("⏰ Jam"),
            "cnt": st.column_config.ProgressColumn(
                "Total Peminjaman",
                format="%d", 
                min_value=0,
                max_value=max(filtered_df_sorted["cnt"]),
            ),
        }
    )

with col2:
        # Mendapatkan data jumlah penyewaan per musim berdasarkan tahun yang dipilih
    if year_selected == '2011':
        tren_by_season = create_tren_by_season_2011(df_day)
    elif year_selected == '2012':
        tren_by_season = create_tren_by_season_2012(df_day)
    else:
        tren_by_season = create_tren_by_season_total(df_day)

    season_mapping = {1: "🌸 Spring", 2: "☀️ Summer", 3: "🍂 Fall", 4: "❄️ Winter"}
    tren_by_season["season"] = tren_by_season["season"].replace(season_mapping)
    tren_by_season_sorted = tren_by_season.sort_values(by="cnt", ascending=False) #urutkan data
    st.write("🏆 Top Penyewaan Sepeda Berdasarkan Musim")

    st.dataframe(
        tren_by_season_sorted,
        column_order=("season", "cnt"),
        hide_index=True,
        width=None,
        column_config={
            "season": st.column_config.TextColumn("🌍 Musim"),
            "cnt": st.column_config.ProgressColumn(
                "Total Peminjaman",
                format="%d",  # Format angka tanpa desimal
                min_value=0,
                max_value=max(tren_by_season_sorted["cnt"]),
            ),
        }
    )
