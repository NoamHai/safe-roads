// Internationalization dictionary
const translations = {
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
    value_unknown: "Unknown",

    // Additional keys
    lowRiskLabel: "Low Risk",
    highRiskLabel: "High Risk",
    errorNetworkTitle: "Unable to Calculate Risk",
    errorNetworkText: "Please check your connection and try again.",
    riskFactorsTitle: "Risk Factors",
    riskFactorsEmpty: "No significant risk factors detected",
    riskLevelLow: "Low risk",
    riskLevelMedium: "Medium risk",
    riskLevelHigh: "High risk"
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
    value_unknown: "לא ידוע",

    // Additional keys
    lowRiskLabel: "סיכון נמוך",
    highRiskLabel: "סיכון גבוה",
    errorNetworkTitle: "לא ניתן לחשב סיכון",
    errorNetworkText: "אנא בדוק את החיבור שלך ונסה שוב.",
    riskFactorsTitle: "גורמי סיכון",
    riskFactorsEmpty: "לא זוהו גורמי סיכון משמעותיים",
    riskLevelLow: "סיכון נמוך",
    riskLevelMedium: "סיכון בינוני",
    riskLevelHigh: "סיכון גבוה"
  }
};

// ========== SINGLE SOURCE OF TRUTH ==========
// These two variables control ALL UI rendering. No other flags are allowed.
let lastPredictionData = null;      // stores last successful API response
let hasPredictionError = false;     // true ONLY if last prediction failed

// Language management functions
function setLanguage(lang) {
  if (!translations[lang]) {
    console.error(`Language '${lang}' not found`);
    return;
  }
  
  console.log(`=== setLanguage(${lang}) called ===`);
  console.log('State:', { hasData: !!lastPredictionData, hasError: hasPredictionError });
  
  // Update HTML attributes
  document.documentElement.lang = lang;
  document.documentElement.dir = lang === 'he' ? 'rtl' : 'ltr';
  
  // Update ONLY static translations (elements with data-i18n that are NOT dynamic prediction data)
  // Dynamic elements (advice, riskBadge) will be updated by renderPrediction if we have data
  const dynamicElementIds = ['advice', 'riskBadge'];
  
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.getAttribute('data-i18n');
    
    // Skip dynamic elements - they'll be handled by state rendering
    if (dynamicElementIds.includes(element.id)) {
      return;
    }
    
    // Update static UI translations
    if (translations[lang][key]) {
      element.textContent = translations[lang][key];
    }
  });
  
  // Update language toggle buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
  });
  
  // Handle prediction state based on single source of truth
  if (lastPredictionData !== null) {
    // We have prediction data - re-render with new language
    console.log('Re-rendering prediction with new language');
    renderPrediction(lastPredictionData);
  }
  
  // STRICT RULE: Error UI may ONLY be shown if hasPredictionError === true
  if (DOM.errorText) {
    if (hasPredictionError === true) {
      DOM.errorText.style.display = "block";
      console.log('Showing error state (hasPredictionError === true)');
    } else {
      DOM.errorText.style.display = "none";
      console.log('Hiding error state (hasPredictionError === false)');
    }
  }
  
  // Save to localStorage
  localStorage.setItem('ui_language', lang);
  
  console.log(`Language set to: ${lang}`);
}

// Function to get friendly factor display
function getFactorDisplay(factor, value, delta, lang) {
  const factorLabelKey = `factor_${factor}`;
  const valueKey = `value_${value}`;
  
  const label = translations[lang][factorLabelKey] || factor;
  const displayValue = translations[lang][valueKey] || value;
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
  
  // Clear previous content
  explainDiv.innerHTML = '';
  
  if (!breakdown || breakdown.length === 0) {
    explainDiv.innerHTML = `<p>${translations[lang].riskFactorsEmpty}</p>`;
    return;
  }
  
  const ul = document.createElement('ul');
  ul.className = 'risk-factors-list';
  
  breakdown
    .filter(item => item && typeof item === "object")
    .forEach(item => {
      const factor = safeToString(item.factor, "unknown");
      const value = safeToString(item.value, "unknown");
      const delta = safeToNumber(item.delta, 0);
      
      const factorLabel = translations[lang][`factor_${factor}`] || factor;
      const valueLabel = translations[lang][`value_${value}`] || value;
      const deltaPercent = Math.round(delta * 100);
      
      const li = document.createElement('li');
      li.textContent = `${factorLabel}: ${valueLabel} (${deltaPercent >= 0 ? '+' : ''}${deltaPercent}%)`;
      
      ul.appendChild(li);
    });
  
  explainDiv.appendChild(ul);
}

// ========== STATE MANAGEMENT ARCHITECTURE ==========
// Global DOM references (initialized on app load)
let DOM = {
  btn: null,
  btnText: null,
  btnLoading: null,
  riskText: null,
  riskBar: null,
  riskBadge: null,
  advice: null,
  errorText: null,
  explainDiv: null
};

// Initialize DOM references
function initializeDOMReferences() {
  DOM.btn = document.getElementById("btn");
  DOM.btnText = document.querySelector(".btn-text");
  DOM.btnLoading = document.querySelector(".btn-loading");
  DOM.riskText = document.getElementById("riskText");
  DOM.riskBar = document.getElementById("riskBar");
  DOM.riskBadge = document.getElementById("riskBadge");
  DOM.advice = document.getElementById("advice");
  DOM.errorText = document.getElementById("errorText");
  DOM.explainDiv = document.getElementById("explain");
  
  console.log("DOM references initialized:", {
    btn: !!DOM.btn,
    btnText: !!DOM.btnText,
    btnLoading: !!DOM.btnLoading,
    riskText: !!DOM.riskText,
    riskBar: !!DOM.riskBar,
    riskBadge: !!DOM.riskBadge,
    advice: !!DOM.advice,
    errorText: !!DOM.errorText,
    explainDiv: !!DOM.explainDiv
  });
}

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
    label: translations[currentLang].low_risk_label, 
    badge: translations[currentLang].low, 
    color: "#2e7d32", 
    cssClass: "risk-low" 
  };
  if (p < 0.66) return { 
    label: translations[currentLang].medium_risk_label, 
    badge: translations[currentLang].medium, 
    color: "#ed6c02", 
    cssClass: "risk-medium" 
  };
  return { 
    label: translations[currentLang].high_risk_label, 
    badge: translations[currentLang].high, 
    color: "#d32f2f", 
    cssClass: "risk-high" 
  };
}

function setAdvice(p) {
  const currentLang = document.documentElement.lang || 'en';
  if (p < 0.33) return translations[currentLang].low_risk_advice;
  if (p < 0.66) return translations[currentLang].medium_risk_advice;
  return translations[currentLang].high_risk_advice;
}

// ========== RENDERING PIPELINE ==========
// ONE rendering function - all prediction UI updates go through here
function renderPrediction(data) {
  if (!data || !data.probability) return;
  
  const currentLang = document.documentElement.lang || 'en';
  const { riskText, riskBar, riskBadge, advice, explainDiv } = DOM;
  
  const p = data.probability;
  const percent = Math.round(p * 100);
  const cls = classifyRisk(p);
  
  // Update percentage text
  if (riskText) {
    riskText.textContent = `${percent}% (${cls.label})`;
    riskText.style.color = cls.color;
  }
  
  // Update risk level text using translations[currentLang]
  if (riskBadge) {
    riskBadge.textContent = cls.badge;
    riskBadge.className = `risk-badge ${cls.cssClass}`;
  }
  
  // Update progress bar
  if (riskBar) {
    riskBar.style.width = `${percent}%`;
    riskBar.style.background = cls.color;
  }
  
  // Update advice
  if (advice) {
    advice.textContent = setAdvice(p);
  }
  
  // Render risk factors
  if (data.breakdown) {
    renderBreakdown(data.breakdown);
  }
  
  // Update risk factors accent color to match current risk level
  if (explainDiv) {
    // Remove all risk level classes
    explainDiv.classList.remove('risk-factors--low', 'risk-factors--medium', 'risk-factors--high');
    // Add the current risk level class
    explainDiv.classList.add(`risk-factors--${cls.cssClass.replace('risk-', '')}`);
  }
  
  console.log("Rendered prediction:", { probability: data.probability, percent, lang: currentLang, riskClass: cls.cssClass });
}

// Initialize language on page load
function initializeLanguage() {
  const savedLang = localStorage.getItem('ui_language') || 'en';
  setLanguage(savedLang);
}

// ========== API CONFIGURATION ==========
function getApiEndpoint() {
  const currentPort = window.location.port;
  const currentHost = window.location.hostname;

  console.log("=== API Endpoint Detection ===");
  console.log("Current URL:", window.location.href);
  console.log("Current Host:", currentHost);
  console.log("Current Port:", currentPort);

  // If served from backend (port 8000), use relative URL
  if (currentPort === '8000') {
    console.log("Using relative URL (same origin)");
    return '/predict';
  }

  // If served from Live Server or other (port 5500, etc.), use full backend URL
  const endpoint = `http://${currentHost}:8000/predict`;
  console.log("Using full backend URL:", endpoint);
  return endpoint;
}

const API_ENDPOINT = getApiEndpoint();
console.log("Final API_ENDPOINT:", API_ENDPOINT);

// ========== PREDICTION LOGIC ==========
async function predict() {
  console.log("=== PREDICT FUNCTION CALLED ===");

  // Check if DOM references are initialized
  if (!DOM.btn || !DOM.riskText || !DOM.errorText) {
    console.error("DOM references not initialized!");
    return;
  }

  const currentLang = document.documentElement.lang || 'en';
  
  // STRICT RULE: Clear previous state
  hasPredictionError = false;
  lastPredictionData = null;
  
  // Hide error (hasPredictionError is now false)
  if (DOM.errorText) {
    DOM.errorText.style.display = "none";
    console.log('Error hidden at start of new prediction');
  }
  
  // Show loading state
  DOM.btn.disabled = true;
  DOM.btnText.style.display = "none";
  DOM.btnLoading.style.display = "inline";
  
  // Reset UI to loading
  if (DOM.riskText) {
    DOM.riskText.textContent = "…";
    DOM.riskText.style.color = "";
  }
  if (DOM.riskBadge) {
    DOM.riskBadge.textContent = translations[currentLang].ready;
    DOM.riskBadge.className = "risk-badge";
  }
  if (DOM.riskBar) {
    DOM.riskBar.style.width = "0%";
    DOM.riskBar.style.background = "#2f6fed";
  }
  if (DOM.advice) {
    DOM.advice.textContent = translations[currentLang].calculating;
  }
  if (DOM.explainDiv) {
    DOM.explainDiv.textContent = "";
  }

  const payload = {
    road_type: document.getElementById("road_type").value,
    weather: document.getElementById("weather").value,
    time_of_day: document.getElementById("time_of_day").value,
    lighting: document.getElementById("lighting").value,
    junction: document.getElementById("junction").value,
    road_surface: document.getElementById("road_surface").value
  };

  try {
    console.log("=== PREDICTION REQUEST ===");
    console.log("Endpoint:", API_ENDPOINT);
    console.log("Payload:", JSON.stringify(payload, null, 2));
    
    const res = await fetch(API_ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    console.log("=== RESPONSE RECEIVED ===");
    console.log("Status:", res.status, res.statusText);
    console.log("Headers:", Object.fromEntries(res.headers.entries()));

    if (!res.ok) {
      let errorMessage = `HTTP ${res.status}`;
      try {
        const errorText = await res.text();
        console.log("Error response body:", errorText);
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
      console.log("=== RESPONSE DATA ===");
      console.log(JSON.stringify(data, null, 2));
    } catch (jsonError) {
      console.error("JSON parse error:", jsonError);
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
    const breakdown = Array.isArray(data.breakdown) ? data.breakdown : [];
    
    // STRICT RULE: Update state first
    lastPredictionData = {
      probability: p,
      breakdown: breakdown
    };
    hasPredictionError = false;
    
    // STRICT RULE: Hide error after ANY successful prediction
    if (DOM.errorText) {
      DOM.errorText.style.display = "none";
      console.log('Error hidden after successful prediction');
    }
    
    // Render success state
    renderPrediction(lastPredictionData);
    
    console.log("=== PREDICTION SUCCESS ===");
  } catch (e) {
    console.error("=== PREDICTION ERROR ===", e);

    // Determine error type and message
    let userMessage = translations[currentLang].error_prediction;
    let errorType = 'unknown';

    if (e.name === 'TypeError' && e.message.includes('fetch')) {
      userMessage = translations[currentLang].network_error;
      errorType = 'network';
      console.error("Network error - likely backend server not running or CORS issue");
    } else if (e.message.includes('HTTP')) {
      userMessage = translations[currentLang].server_error;
      errorType = 'server';
      console.error("Server error - check backend logs");
    } else if (e.message.includes('JSON') || e.message.includes('invalid')) {
      userMessage = translations[currentLang].invalid_response;
      errorType = 'response';
      console.error("Invalid response format from server");
    }

    console.error(`Error type: ${errorType}, User message: ${userMessage}`);

    // STRICT RULE: Update state first, then show error ONLY if hasPredictionError === true
    hasPredictionError = true;
    lastPredictionData = null;
    
    // Show error state (ONLY because hasPredictionError === true)
    if (DOM.errorText && hasPredictionError === true) {
      DOM.errorText.style.display = "block";
    }
    if (DOM.advice) DOM.advice.textContent = userMessage;
    if (DOM.riskBadge) {
      DOM.riskBadge.textContent = translations[currentLang].error;
      DOM.riskBadge.className = "risk-badge risk-error";
    }
  } finally {
    // Re-enable button
    DOM.btn.disabled = false;
    DOM.btnText.style.display = "inline";
    DOM.btnLoading.style.display = "none";
  }
}

// ========== APP INITIALIZATION ==========
function initializeApp() {
  console.log("=== INITIALIZING APP ===");
  
  // Initialize DOM references
  initializeDOMReferences();



  // Initialize language
  initializeLanguage();

  // Add language toggle event listeners
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      const lang = this.getAttribute('data-lang');
      setLanguage(lang);
    });
  });

  // Attach event listener to predict button
  if (DOM.btn) {
    DOM.btn.addEventListener("click", function(event) {
      event.preventDefault();
      console.log("Predict button clicked!");
      predict();
    });
    console.log("Predict button event listener attached");
  } else {
    console.error("Predict button not found!");
  }

  console.log("=== APP INITIALIZED SUCCESSFULLY ===");
}

// Check if DOM is already loaded (since script is loaded at end of body)
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeApp);
} else {
  // DOM is already loaded
  initializeApp();
}
