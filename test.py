import streamlit as st

# Cơ sở dữ liệu giả định các phim
phim_data = {
    'Phim 1': ['Thể loại 1', 'Thể loại 2'],
    'Phim 2': ['Thể loại 2', 'Thể loại 3'],
    'Phim 3': ['Thể loại 1', 'Thể loại 3'],
    'Phim 4': ['Thể loại 4'],
    'Phim 5': ['Thể loại 2'],
}

# Hàm recommend phim dựa trên sở thích
def recommend_phim(su_thich):
    recommended_movies = []
    for ten_phim, the_loai in phim_data.items():
        for the_loai_phim in the_loai:
            if the_loai_phim in su_thich and ten_phim not in recommended_movies:
                recommended_movies.append(ten_phim)
    return recommended_movies

def main():
    st.title("Recommend Phim")

    # Hiển thị danh sách phim
    st.header("Danh sách phim:")
    st.write(list(phim_data.keys()))

    # Nhập sở thích người dùng
    su_thich = st.multiselect("Chọn sở thích của bạn:", list(set([the_loai for the_loai_list in phim_data.values() for the_loai in the_loai_list])))

    # Gợi ý phim dựa trên sở thích
    if su_thich:
        recommended_movies = recommend_phim(su_thich)
        if recommended_movies:
            st.header("Phim được gợi ý:")
            st.write(recommended_movies)
        else:
            st.info("Không có phim nào được gợi ý dựa trên sở thích của bạn.")

if __name__ == '__main__':
    main()
