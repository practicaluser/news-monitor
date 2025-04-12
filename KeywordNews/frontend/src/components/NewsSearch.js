// src/components/NewsSearch.js
import React, { useState } from 'react'
import axios from 'axios'

function NewsSearch() {
  const [keyword, setKeyword] = useState('')
  const [newsList, setNewsList] = useState([])
  const [loading, setLoading] = useState(false)

  const handleSearch = async () => {
    if (!keyword.trim()) return
    setLoading(true)
    try {
      const response = await axios.get(
        `http://localhost:8000/api/get-news/?keyword=${encodeURIComponent(
          keyword,
        )}`,
      )
      setNewsList(response.data)
    } catch (error) {
      console.error('뉴스 가져오기 실패:', error)
      alert('뉴스를 불러오는 데 실패했습니다.')
    }
    setLoading(false)
  }

  return (
    <div className="p-4 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">키워드 뉴스 검색</h1>
      <div className="flex gap-2 mb-4">
        <input
          type="text"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          placeholder="검색어를 입력하세요"
          className="flex-grow border border-gray-300 px-4 py-2 rounded"
        />
        <button
          onClick={handleSearch}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          검색
        </button>
      </div>

      {loading && <p className="text-gray-500">불러오는 중...</p>}
      {!loading && newsList.length === 0 && (
        <p className="text-gray-400">뉴스가 없습니다.</p>
      )}

      <ul className="space-y-4 mt-4">
        {newsList.map((news, index) => (
          <li
            key={index}
            className="border p-4 rounded shadow-sm bg-white hover:bg-gray-50 transition"
          >
            <a
              href={news.link}
              target="_blank"
              rel="noopener noreferrer"
              className="text-lg font-semibold text-blue-600 hover:underline"
            >
              {news.title}
            </a>
            <p className="text-sm mt-2 text-gray-700">{news.summary}</p>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default NewsSearch
