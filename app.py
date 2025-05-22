import streamlit as st
from utils.rag import retrieve_relevant_chunks, generate_answer

st.title("📚 Q&A System with RAG + Vector DB")

question = st.text_input("Masukkan pertanyaanmu:")

if st.button("Cari Jawaban") and question:
    with st.spinner("Sedang mencari jawaban..."):
        chunks = retrieve_relevant_chunks(question)
        answer = generate_answer(question, chunks)

        st.subheader("Jawaban:")
        st.write(answer)

        st.subheader("Sumber Dokumen:")
        for i, chunk in enumerate(chunks):
            st.markdown(f"**Chunk {i+1}:** {chunk.get('text', '-')}")
            st.caption(f"Sumber: {chunk.get('doc_name', '-')}")
