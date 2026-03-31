// Internationalization dictionary
const i18n = {
  en: {
    // Header
    choose_language: "Choose a language",
    title: "Safe Roads",
    subtitle: "Real-time Accident Risk Assessment",
    
    // Input section
    driving_conditions: "Driving Conditions",
    select_conditions: "Select your current driving conditions to get an instant risk assessment.",
    road_type: "Road Type",
    urban: "Urban",
    highway: "Highway",
    weather: "Weather",
    clear: "Clear",
    rain: "Rain",
    fog: "Fog",
    time_of_day: "Time of Day",
    day: "Day",
    night: "Night",
    lighting: "Lighting",
    daylight: "Daylight",
    dark_streetlights: "Dark (streetlights)",
    dark_no_streetlights: "Dark (no streetlights)",
    junction: "Junction",
    no_junction: "No junction",
    junction_area: "Junction area",
    road_surface: "Road Surface",
    dry: "Dry",
    wet: "Wet",
    unknown: "Unknown",
    predict_risk: "Predict Risk",
    analyzing: "Analyzing...",
    
    // Result section
    risk_assessment: "Risk Assessment",
    risk_level: "Risk Level",
    ready: "Ready",
    low_risk: "Low Risk",
    high_risk: "High Risk",
    recommendation: "Recommendation",
    select_conditions_advice: "Select your driving conditions and click \"Predict Risk\" to get personalized safety recommendations.",
    risk_factors: "Risk Factors",
    
    // Dynamic text
    calculating: "Calculating prediction…",
    why_this_risk: "Why this risk?",
    error_prediction: "Could not get prediction. Make sure the backend is running.",
    error: "Error",
    
    // Risk levels
    low_risk_label: "Low risk",
    medium_risk_label: "Medium risk", 
    high_risk_label: "High risk",
    low: "Low",
    medium: "Medium",
    high: "High",
    
    // Advice
    low_risk_advice: "Low risk. Drive normally and stay alert.",
    medium_risk_advice: "Medium risk. Reduce speed and stay focused.",
    high_risk_advice: "High risk. Drive carefully and avoid distractions.",
    
    // Error messages
    unable_calculate: "Unable to Calculate Risk",
    check_connection: "Please check your connection and try again.",
    network_error: "Network connection failed. Please check if the backend server is running.",
    server_error: "Server error occurred. Please try again later.",
    invalid_response: "Received invalid response from server.",

    // Factor labels for risk breakdown
    factor_road_type: "Road Type",
    factor_weather: "Weather", 
    factor_time_of_day: "Time of Day",
    factor_lighting: "Lighting",
    factor_junction: "Junction",
    factor_road_surface: "Road Surface",

    // Factor values
    value_urban: "Urban",
    value_highway: "Highway",
    value_clear: "Clear",
    value_rain: "Rain", 
    value_fog: "Fog",
    value_day: "Day",
    value_night: "Night",
    value_daylight: "Daylight",
    value_dark_streetlights: "Dark (streetlights)",
    value_dark_no_streetlights: "Dark (no streetlights)",
    value_no_junction: "No junction",
    value_junction_area: "Junction area",
    value_dry: "Dry",
    value_wet: "Wet",
    value_unknown: "Unknown"
  },
  he: {
    // Header
    choose_language: "בחר שפה",
    title: "כבישים בטוחים",
    subtitle: "הערכת סיכון תאונות בזמן אמת",
    
    // Input section
    driving_conditions: "תנאי נהיגה",
    select_conditions: "בחר את תנאי הנהיגה הנוכחיים שלך כדי לקבל הערכת סיכון מיידית.",
    road_type: "סוג כביש",
    urban: "עירוני",
    highway: "כביש מהיר",
    weather: "מזג אוויר",
    clear: "בהיר",
    rain: "גשם",
    fog: "ערפל",
    time_of_day: "זמן ביום",
    day: "יום",
    night: "לילה",
    lighting: "תאורה",
    daylight: "אור יום",
    dark_streetlights: "חושך (עם פנסי רחוב)",
    dark_no_streetlights: "חושך (ללא פנסי רחוב)",
    junction: "צומת",
    no_junction: "אין צומת",
    junction_area: "אזור צומת",
    road_surface: "מצב הכביש",
    dry: "יבש",
    wet: "רטוב",
    unknown: "לא ידוע",
    predict_risk: "חשב סיכון",
    analyzing: "מחשב...",
    
    // Result section
    risk_assessment: "הערכת סיכון",
    risk_level: "רמת סיכון",
    ready: "מוכן",
    low_risk: "סיכון נמוך",
    high_risk: "סיכון גבוה",
    recommendation: "המלצה",
    select_conditions_advice: "בחר את תנאי הנהיגה שלך ולחץ על \"חשב סיכון\" כדי לקבל המלצות בטיחות מותאמות אישית.",
    risk_factors: "גורמי סיכון",
    
    // Dynamic text
    calculating: "מחשב הערכה…",
    why_this_risk: "למה סיכון זה?",
    error_prediction: "לא ניתן לקבל הערכה. וודא שהשרת פועל.",
    error: "שגיאה",
    
    // Risk levels
    low_risk_label: "סיכון נמוך",
    medium_risk_label: "סיכון בינוני",
    high_risk_label: "סיכון גבוה",
    low: "נמוך",
    medium: "בינוני",
    high: "גבוה",
    
    // Advice
    low_risk_advice: "סיכון נמוך. נהג כרגיל והישאר ערני.",
    medium_risk_advice: "סיכון בינוני. האט את המהירות והתמקד.",
    high_risk_advice: "סיכון גבוה. נהג בזהירות והימנע מהסחות דעת.",
    
    // Error messages
    unable_calculate: "לא ניתן לחשב סיכון",
    check_connection: "אנא בדוק את החיבור שלך ונסה שוב.",
    network_error: "החיבור לרשת נכשל. אנא בדוק אם שרת ה-backend פועל.",
    server_error: "אירעה שגיאת שרת. אנא נסה שוב מאוחר יותר.",
    invalid_response: "התקבלה תגובה לא תקינה מהשרת.",

    // Factor labels for risk breakdown
    factor_road_type: "סוג כביש",
    factor_weather: "מזג אוויר",
    factor_time_of_day: "זמן ביום",
    factor_lighting: "תאורה",
    factor_junction: "צומת",
    factor_road_surface: "מצב הכביש",

    // Factor values
    value_urban: "עירוני",
    value_highway: "כביש מהיר",
    value_clear: "בהיר",
    value_rain: "גשם",
    value_fog: "ערפל",
    value_day: "יום",
    value_night: "לילה",
    value_daylight: "אור יום",
    value_dark_streetlights: "חושך (עם פנסי רחוב)",
    value_dark_no_streetlights: "חושך (ללא פנסי רחוב)",
    value_no_junction: "אין צומת",
    value_junction_area: "אזור צומת",
    value_dry: "יבש",
    value_wet: "רטוב",
    value_unknown: "לא ידוע"
  }
};

// Language management functions
function setLanguage(lang) {
  if (!i18n[lang]) {
    console.error(`Language '${lang}' not found`);
    return;
  }
  
  // Update HTML attributes
  document.documentElement.lang = lang;
  document.documentElement.dir = lang === 'he' ? 'rtl' : 'ltr';
  
  // Update all elements with data-i18n
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.getAttribute('data-i18n');
    if (i18n[lang][key]) {
      element.textContent = i18n[lang][key];
    }
  });
  
  // Update language toggle buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
  });
  
  // Update dynamic content if it exists
  updateDynamicContent();
  
  // Save to localStorage
  localStorage.setItem('ui_language', lang);
  
  console.log(`Language set to: ${lang}`);
}

// Function to get friendly factor display
function getFactorDisplay(factor, value, delta, lang) {
  const factorLabelKey = `factor_${factor}`;
  const valueKey = `value_${value}`;
  
  const label = i18n[lang][factorLabelKey] || factor;
  const displayValue = i18n[lang][valueKey] || value;
  const deltaPercent = Math.round(delta * 100);
  
  return {
    label: label,
    value: displayValue,
    impact: deltaPercent
  };
}

// Function to render breakdown factors
function renderBreakdown(breakdown) {
  const explainDiv = document.getElementById("explain");
  const lang = document.documentElement.lang || 'en';
  
  explainDiv.innerHTML = `<div class="risk-factors-title">${i18n[lang].why_this_risk}</div>`;
  
  const factorsList = document.createElement('div');
  factorsList.className = 'risk-factors-list';
  
  breakdown
    .filter(item => item && typeof item === "object")
    .forEach(item => {
      const factor = safeToString(item.factor, "unknown");
      const value = safeToString(item.value, "unknown");
      const delta = safeToNumber(item.delta, 0);
      
      const display = getFactorDisplay(factor, value, delta, lang);
      
      const factorItem = document.createElement('div');
      factorItem.className = 'risk-factor-item';
      factorItem.innerHTML = `
        <div class="factor-label">${display.label}</div>
        <div class="factor-value">${display.value}</div>
        <div class="factor-impact ${display.impact >= 0 ? 'positive' : 'negative'}">+${display.impact}%</div>
      `;
      
      factorsList.appendChild(factorItem);
    });
  
  explainDiv.appendChild(factorsList);
}

// Global variable to store last breakdown data
let lastBreakdownData = null;

// Function to update dynamic content when language changes
function updateDynamicContent() {
  const lang = document.documentElement.lang || 'en';
  
  // Update risk badge if it exists
  const riskBadge = document.getElementById("riskBadge");
  if (riskBadge && riskBadge.textContent && riskBadge.textContent !== "...") {
    // Re-classify based on current language
    const riskText = document.getElementById("riskText");
    if (riskText && riskText.textContent) {
      const percentMatch = riskText.textContent.match(/(\d+)%/);
      if (percentMatch) {
        const percent = parseInt(percentMatch[1]);
        const p = percent / 100;
        const cls = classifyRisk(p);
        riskBadge.textContent = cls.badge;
      }
    }
  }
  
  // Update advice if it exists
  const advice = document.getElementById("advice");
  if (advice && advice.textContent && !advice.textContent.includes("Select") && !advice.textContent.includes("בחר")) {
    const riskText = document.getElementById("riskText");
    if (riskText && riskText.textContent) {
      const percentMatch = riskText.textContent.match(/(\d+)%/);
      if (percentMatch) {
        const percent = parseInt(percentMatch[1]);
        const p = percent / 100;
        advice.textContent = setAdvice(p);
      }
    }
  }
  
  // Re-render risk factors if we have stored data
  if (lastBreakdownData && lastBreakdownData.length > 0) {
    renderBreakdown(lastBreakdownData);
  }
}

// Initialize language on page load
function initializeLanguage() {
  const savedLang = localStorage.getItem('ui_language') || 'en';
  setLanguage(savedLang);
}

function initializeApp() {
  // Get DOM elements
  const btn = document.getElementById("btn");
  const btnText = document.querySelector(".btn-text");
  const btnLoading = document.querySelector(".btn-loading");
  const riskText = document.getElementById("riskText");
  const riskBar = document.getElementById("riskBar");
  const riskBadge = document.getElementById("riskBadge");
  const errorText = document.getElementById("errorText");
  const advice = document.getElementById("advice");
  const explainDiv = document.getElementById("explain");

  // Check if all required elements exist
  console.log("DOM elements check:");
  console.log("- btn:", !!btn);
  console.log("- btnText:", !!btnText);
  console.log("- btnLoading:", !!btnLoading);
  console.log("- riskText:", !!riskText);
  console.log("- riskBar:", !!riskBar);
  console.log("- riskBadge:", !!riskBadge);
  console.log("- errorText:", !!errorText);
  console.log("- advice:", !!advice);
  console.log("- explainDiv:", !!explainDiv);

  // API endpoint - dynamically set based on environment
  function getApiEndpoint() {
    const currentPort = window.location.port;
    const currentHost = window.location.hostname;

    // If served from backend (port 8000), use relative URL
    if (currentPort === '8000') {
      return '/predict';
    }

    // If served from Live Server or other (port 5500, etc.), use full backend URL
    return `http://${currentHost}:8001/predict`;
  }

  const API_ENDPOINT = getApiEndpoint();

  // Utility function to check if a value is a finite number in [0,1]
  function isValidProbability(value) {
    return typeof value === "number" && isFinite(value) && value >= 0 && value <= 1;
  }

  // Utility function to safely convert to number, defaulting to 0
  function safeToNumber(value, defaultValue = 0) {
    const num = Number(value);
    return isFinite(num) ? num : defaultValue;
  }

  // Utility function to safely get string value
  function safeToString(value, defaultValue = "") {
    return typeof value === "string" ? value : String(value || defaultValue);
  }

  function classifyRisk(p) {
    const currentLang = document.documentElement.lang || 'en';
    if (p < 0.33) return { 
      label: i18n[currentLang].low_risk_label, 
      badge: i18n[currentLang].low, 
      color: "#2e7d32", 
      cssClass: "risk-low" 
    };
    if (p < 0.66) return { 
      label: i18n[currentLang].medium_risk_label, 
      badge: i18n[currentLang].medium, 
      color: "#ed6c02", 
      cssClass: "risk-medium" 
    };
    return { 
      label: i18n[currentLang].high_risk_label, 
      badge: i18n[currentLang].high, 
      color: "#d32f2f", 
      cssClass: "risk-high" 
    };
  }

  function setAdvice(p) {
    const currentLang = document.documentElement.lang || 'en';
    if (p < 0.33) return i18n[currentLang].low_risk_advice;
    if (p < 0.66) return i18n[currentLang].medium_risk_advice;
    return i18n[currentLang].high_risk_advice;
  }

  async function predict() {
    console.log("predict() function called"); // Debug log

    // Check if all required elements exist
    if (!btn || !btnText || !btnLoading || !riskText || !riskBar || !riskBadge || !errorText || !advice || !explainDiv) {
      console.error("Missing DOM elements!");
      return;
    }

    errorText.style.display = "none";
    btn.disabled = true;
    btnText.style.display = "none";
    btnLoading.style.display = "inline";
    riskText.textContent = "…";
    riskText.style.color = "";
    riskBadge.textContent = i18n[document.documentElement.lang || 'en'].ready;
    riskBadge.className = "risk-badge"; // Reset classes
    riskBar.style.width = "0%";
    riskBar.style.background = "#2f6fed";
    advice.textContent = i18n[document.documentElement.lang || 'en'].calculating;
    explainDiv.textContent = "";

    const payload = {
      road_type: document.getElementById("road_type").value,
      weather: document.getElementById("weather").value,
      time_of_day: document.getElementById("time_of_day").value,
      lighting: document.getElementById("lighting").value,
      junction: document.getElementById("junction").value,
      road_surface: document.getElementById("road_surface").value
    };

    try {
      console.log("About to fetch:", API_ENDPOINT, "with payload:", payload); // Debug log
      const res = await fetch(API_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (!res.ok) {
        let errorMessage = `HTTP ${res.status}`;
        try {
          const errorText = await res.text();
          if (errorText) {
            errorMessage += `: ${errorText}`;
          }
        } catch (textError) {
          // Ignore text parsing errors
        }
        throw new Error(errorMessage);
      }

      let data;
      try {
        data = await res.json();
      } catch (jsonError) {
        throw new Error("Server returned invalid JSON response");
      }

      // Validate response structure
      if (!data || typeof data !== "object") {
        throw new Error("Server returned invalid response format");
      }

      // Validate and extract probability
      const rawProbability = data.probability;
      if (!isValidProbability(rawProbability)) {
        throw new Error(`Server returned invalid probability: ${rawProbability}`);
      }

      const p = rawProbability;
      const percent = Math.round(p * 100);

      const cls = classifyRisk(p);

      riskText.textContent = `${percent}% (${cls.label})`;
      riskText.style.color = cls.color;

      riskBadge.textContent = cls.badge;
      riskBadge.className = `risk-badge ${cls.cssClass}`;

      riskBar.style.width = `${percent}%`;
      riskBar.style.background = cls.color;

      advice.textContent = setAdvice(p);

      // Defensive breakdown rendering
      const breakdown = Array.isArray(data.breakdown) ? data.breakdown : [];
      if (breakdown.length > 0) {
        lastBreakdownData = breakdown; // Store for language switching
        renderBreakdown(breakdown);
      }
    } catch (e) {
      console.error("Prediction error:", e);

      // Determine error type and show appropriate message
      let userMessage = i18n[document.documentElement.lang || 'en'].error_prediction;
      let errorType = 'unknown';

      if (e.name === 'TypeError' && e.message.includes('fetch')) {
        // Network/connection error
        userMessage = i18n[document.documentElement.lang || 'en'].network_error;
        errorType = 'network';
        console.error("Network error - likely backend server not running or CORS issue");
      } else if (e.message.includes('HTTP')) {
        // Server returned error status
        userMessage = i18n[document.documentElement.lang || 'en'].server_error;
        errorType = 'server';
        console.error("Server error - check backend logs");
      } else if (e.message.includes('JSON') || e.message.includes('invalid')) {
        // Invalid response format
        userMessage = i18n[document.documentElement.lang || 'en'].invalid_response;
        errorType = 'response';
        console.error("Invalid response format from server");
      }

      console.error(`Error type: ${errorType}, User message: ${userMessage}`);

      errorText.style.display = "block";
      advice.textContent = userMessage;
      riskBadge.textContent = i18n[document.documentElement.lang || 'en'].error;
      riskBadge.className = "risk-badge risk-error";
    } finally {
      btn.disabled = false;
      btnText.style.display = "inline";
      btnLoading.style.display = "none";
    }
  }

  // Initialize language
  initializeLanguage();

  // Add language toggle event listeners
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      const lang = this.getAttribute('data-lang');
      setLanguage(lang);
    });
  });

  // Attach event listener only if button exists
  if (btn) {
    btn.addEventListener("click", function(event) {
      event.preventDefault(); // Prevent any default form submission
      console.log("Predict button clicked!"); // Debug log
      predict();
    });
  } else {
    console.error("Button with id 'btn' not found!");
  }

  console.log("script.js loaded and initialized");
}

// Check if DOM is already loaded (since script is loaded at end of body)
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeApp);
} else {
  // DOM is already loaded
  initializeApp();
}
