// 所有游戏数据
const allGames = {
    // Adventure Games
    "conquer-kingdoms": {
        title: "Conquer Kingdoms",
        description: "Build your kingdom, train your army, battle your enemies, and become the ruler!",
        category: "Adventure",
        image: "images/conquer-kingdoms.jpg"
    },
    "miniblox-io": {
        title: "Miniblox IO",
        description: "Explore, build, battle, and play with friends in this pixel world!",
        category: "Adventure",
        image: "images/miniblox-io.jpg"
    },
    // Clicker Games
    "capybara-clicker-pro": {
        title: "Capybara Clicker Pro",
        description: "Tap on the adorable Capybara to collect coins. Increase your earnings and unlock new characters!",
        category: "Clicker",
        image: "clicker_images/capybara-clicker-pro.jpg"
    },
    "poop-clicker": {
        title: "Poop Clicker",
        description: "Click on the poo-poo on the screen to earn fantastic rewards as a dedicated plumber!",
        category: "Clicker",
        image: "clicker_images/poop-clicker.jpg"
    },
    // Car Games
    "turbo-race-3d": {
        title: "Turbo Race 3D",
        description: "A simple and fun racing game focused on steering and braking.",
        category: "Car",
        image: "car_games_images/turbo-race-3d.jpg"
    },
    // Sports Games
    "basket-random": {
        title: "Basket Random",
        description: "Play basketball with limited mobility! Control your character with one key and perform amazing dunks.",
        category: "Sports",
        image: "sports_images/basket-random.jpg"
    }
};

// 创建搜索框和结果容器
function createSearchBox() {
    // 创建搜索容器
    const searchContainer = document.createElement('div');
    searchContainer.className = 'search-container';
    
    // 创建搜索框
    const searchBox = document.createElement('input');
    searchBox.type = 'text';
    searchBox.placeholder = 'Search games...';
    searchBox.className = 'search-box';
    
    // 创建搜索结果容器
    const searchResults = document.createElement('div');
    searchResults.className = 'search-results';
    
    // 添加到容器
    searchContainer.appendChild(searchBox);
    searchContainer.appendChild(searchResults);
    
    // 添加到导航栏
    const nav = document.querySelector('nav');
    nav.insertBefore(searchContainer, nav.querySelector('.nav-links'));
    
    // 添加搜索事件监听
    searchBox.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        
        // 清空结果
        searchResults.innerHTML = '';
        
        if (query.length < 2) {
            searchResults.style.display = 'none';
            return;
        }
        
        // 搜索匹配的游戏
        const matches = Object.entries(allGames).filter(([id, game]) => {
            return game.title.toLowerCase().includes(query) || 
                   game.description.toLowerCase().includes(query) ||
                   game.category.toLowerCase().includes(query);
        });
        
        if (matches.length > 0) {
            searchResults.style.display = 'block';
            matches.slice(0, 5).forEach(([id, game]) => {
                const result = document.createElement('div');
                result.className = 'search-result-item';
                result.innerHTML = `
                    <img src="${game.image}" alt="${game.title}">
                    <div class="result-info">
                        <h4>${game.title}</h4>
                        <span class="category">${game.category}</span>
                    </div>
                `;
                result.addEventListener('click', () => {
                    window.location.href = `game.html?id=${id}`;
                });
                searchResults.appendChild(result);
            });
        } else {
            searchResults.style.display = 'none';
        }
    });
    
    // 点击其他地方时隐藏结果
    document.addEventListener('click', (e) => {
        if (!searchContainer.contains(e.target)) {
            searchResults.style.display = 'none';
        }
    });
}

// 页面加载完成后初始化搜索框
document.addEventListener('DOMContentLoaded', createSearchBox); 