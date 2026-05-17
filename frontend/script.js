const i18n = {
  en: {
    choose_language: "Choose a language",
    title: "Safe Roads",
    subtitle: "Real-time Accident Risk Assessment",
    driving_conditions: "Driving Conditions",
    select_conditions: "Select your current driving conditions to get an instant risk assessment.",
    section_time_location: "Time & Location",
    section_road_conditions: "Road Conditions",
    section_accident_details: "Environment & Visibility",
    label_SHAA: "Time",
    label_HODESH_TEUNA: "Month",
    label_YOM_BASHAVUA: "Day of Week",
    label_ZURAT_ISHUV: "Settlement Form",
    label_NAFA: "District",
    label_ROAD_STRUCTURE: "Road Structure",
    label_ROHAV: "Road Width",
    label_MEHIRUT_MUTERET: "Speed Limit",
    label_TEURA: "Lighting",
    label_SUG_DEREH: "Road Type",
    label_PNE_KVISH: "Road Surface",
    label_TKINUT: "Road Condition",
    label_MEZEG_AVIR: "Weather",
    label_YOM_LAYLA: "Day / Night",
    label_SUG_TEUNA: "Accident Type",
    label_SIMUN_TIMRUR: "Traffic Marking",
    predict_risk: "Predict Risk",
    analyzing: "Analyzing...",
    risk_assessment: "Risk Assessment",
    risk_level: "Risk Level",
    ready: "Ready",
    low_risk: "Low Risk",
    medium_risk_label: "Medium Risk",
    high_risk: "High Risk",
    light_accident: "Light Accident",
    dangerous_accident: "Dangerous Accident",
    recommendation: "Recommendation",
    risk_factors: "Risk Factors",
    select_conditions_advice: "Select your driving conditions and click \"Predict Risk\" to get personalized safety recommendations.",
    calculating: "Calculating prediction...",
    why_this_risk: "Why this risk?",
    low_risk_label: "Low risk",
    high_risk_label: "High risk",
    low: "Low",
    medium: "Medium",
    high: "High",
    error: "Error",
    low_risk_advice: "Low risk. Drive normally and stay alert.",
    medium_risk_advice: "Medium risk. Reduce speed and stay focused.",
    high_risk_advice: "High risk. Drive carefully and avoid distractions.",
    unable_calculate: "Unable to Calculate Risk",
    check_connection: "Please check your connection and try again.",
    network_error: "Network connection failed. Please check if the backend server is running.",
    server_error: "Server error occurred. Please try again later.",
    invalid_response: "Received invalid response from server.",
    factor_hour: "Hour",
    factor_month: "Month",
    factor_accident_type: "Accident Type",
    factor_speed_limit: "Speed Limit",
    factor_district: "District",
    validation_required_title: "Please complete all required fields",
    validation_required_message: "Missing fields: {fields}"
  },
  he: {
    choose_language: "בחר שפה",
    title: "כבישים בטוחים",
    subtitle: "הערכת סיכון תאונות בזמן אמת",
    driving_conditions: "תנאי נהיגה",
    select_conditions: "בחר את תנאי הנהיגה הנוכחיים שלך כדי לקבל הערכת סיכון מיידית.",
    section_time_location: "זמן ומיקום",
    section_road_conditions: "תנאי הדרך",
    section_accident_details: "סביבה ונראות",
    label_SHAA: "זמן",
    label_HODESH_TEUNA: "חודש",
    label_YOM_BASHAVUA: "יום בשבוע",
    label_ZURAT_ISHUV: "צורת יישוב",
    label_NAFA: "נפה",
    label_ROAD_STRUCTURE: "מבנה הדרך",
    label_ROHAV: "רוחב כביש",
    label_MEHIRUT_MUTERET: "מהירות מותרת",
    label_TEURA: "תאורה",
    label_SUG_DEREH: "סוג דרך",
    label_PNE_KVISH: "מצב פני הכביש",
    label_TKINUT: "תקינות הדרך",
    label_MEZEG_AVIR: "מזג אוויר",
    label_YOM_LAYLA: "יום / לילה",
    label_SUG_TEUNA: "סוג תאונה",
    label_SIMUN_TIMRUR: "סימון תנועה",
    predict_risk: "חשב סיכון",
    analyzing: "מחשב...",
    risk_assessment: "הערכת סיכון",
    risk_level: "רמת סיכון",
    ready: "מוכן",
    low_risk: "סיכון נמוך",
    medium_risk_label: "סיכון בינוני",
    high_risk: "סיכון גבוה",
    light_accident: "תאונה קלה",
    dangerous_accident: "תאונה מסוכנת",
    recommendation: "המלצה",
    risk_factors: "גורמי סיכון",
    select_conditions_advice: "בחר את תנאי הנהיגה ולחץ על \"חשב סיכון\" כדי לקבל המלצות בטיחות מותאמות אישית.",
    calculating: "מחשב הערכה...",
    why_this_risk: "למה הסיכון הזה?",
    low_risk_label: "סיכון נמוך",
    high_risk_label: "סיכון גבוה",
    low: "נמוך",
    medium: "בינוני",
    high: "גבוה",
    error: "שגיאה",
    low_risk_advice: "הסיכון נמוך. נהג כרגיל והישאר ערני.",
    medium_risk_advice: "הסיכון בינוני. האט ושמור על ריכוז.",
    high_risk_advice: "הסיכון גבוה. נהג בזהירות והימנע מהסחות דעת.",
    unable_calculate: "לא ניתן לחשב סיכון",
    check_connection: "אנא בדוק את החיבור ונסה שוב.",
    network_error: "חיבור הרשת נכשל. בדוק אם שרת ה-backend פועל.",
    server_error: "אירעה שגיאת שרת. נסה שוב מאוחר יותר.",
    invalid_response: "התקבלה תגובה לא תקינה מהשרת.",
    factor_hour: "שעה",
    factor_month: "חודש",
    factor_accident_type: "סוג תאונה",
    factor_speed_limit: "מהירות מותרת",
    factor_district: "מחוז",
    validation_required_title: "אנא מלא/י את כל השדות הנדרשים",
    validation_required_message: "שדות חסרים: {fields}"
  }
};

function buildHourOptions() {
  const rows = [];
  for (let hour = 0; hour <= 23; hour += 1) {
    const label = String(hour).padStart(2, "0");
    rows.push({ value: String(hour), en: label, he: label });
  }
  return rows;
}

function buildMinuteOptions() {
  return [
    { value: "00", en: "00", he: "00" },
    { value: "15", en: "15", he: "15" },
    { value: "30", en: "30", he: "30" },
    { value: "45", en: "45", he: "45" }
  ];
}

function buildMonthOptions() {
  const rows = [];
  for (let month = 1; month <= 12; month += 1) {
    rows.push({ value: String(month), en: String(month), he: String(month) });
  }
  return rows;
}

const selectOptions = {
  SHAA_HOUR: buildHourOptions(),
  SHAA_MINUTE: buildMinuteOptions(),
  HODESH_TEUNA: buildMonthOptions(),
  YOM_BASHAVUA: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "ראשון", en: "Sunday", he: "ראשון" },
    { value: "שני", en: "Monday", he: "שני" },
    { value: "שלישי", en: "Tuesday", he: "שלישי" },
    { value: "רביעי", en: "Wednesday", he: "רביעי" },
    { value: "חמישי", en: "Thursday", he: "חמישי" },
    { value: "שישי", en: "Friday", he: "שישי" },
    { value: "שבת", en: "Saturday", he: "שבת" }
  ],
  ZURAT_ISHUV: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "עירוני", en: "Urban", he: "עירוני" },
    { value: "כפרי", en: "Rural", he: "כפרי" },
    { value: "כביש ראשי", en: "Main Road", he: "כביש ראשי" }
  ],
  NAFA: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "מרכז", en: "Center", he: "מרכז" },
    { value: "צפון", en: "North", he: "צפון" },
    { value: "דרום", en: "South", he: "דרום" },
    { value: "ירושלים", en: "Jerusalem", he: "ירושלים" },
    { value: "חיפה", en: "Haifa", he: "חיפה" }
  ],
  ROAD_STRUCTURE: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "חד-כיווני", en: "One-way", he: "חד-כיווני" },
    { value: "דו-כיווני", en: "Two-way", he: "דו-כיווני" },
    { value: "רב-נתיבים דו-כיווני", en: "Multi-lane Two-way", he: "רב-נתיבים דו-כיווני" },
    { value: "רב-נתיבים חד-כיווני", en: "Multi-lane One-way", he: "רב-נתיבים חד-כיווני" }
  ],
  ROHAV: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "צר (עד 6.5 מ')", en: "Narrow (<=6.5m)", he: "צר (עד 6.5 מ')" },
    { value: "בינוני (6.5-8 מ')", en: "Medium (6.5-8m)", he: "בינוני (6.5-8 מ')" },
    { value: "רחב (מעל 8 מ')", en: "Wide (>8m)", he: "רחב (מעל 8 מ')" }
  ],
  MEHIRUT_MUTERET: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "עד 50 קמ״ש", en: "Up to 50 km/h", he: "עד 50 קמ״ש" },
    { value: "עד 60 קמ״ש", en: "Up to 60 km/h", he: "עד 60 קמ״ש" },
    { value: "עד 70 קמ״ש", en: "Up to 70 km/h", he: "עד 70 קמ״ש" },
    { value: "עד 80 קמ״ש", en: "Up to 80 km/h", he: "עד 80 קמ״ש" },
    { value: "עד 90 קמ״ש", en: "Up to 90 km/h", he: "עד 90 קמ״ש" },
    { value: "עד 100 קמ״ש", en: "Up to 100 km/h", he: "עד 100 קמ״ש" },
    { value: "עד 110 קמ״ש", en: "Up to 110 km/h", he: "עד 110 קמ״ש" },
    { value: "עד 120 קמ״ש", en: "Up to 120 km/h", he: "עד 120 קמ״ש" }
  ],
  TEURA: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "אור יום", en: "Daylight", he: "אור יום" },
    { value: "לילה עם תאורה", en: "Night with lighting", he: "לילה עם תאורה" },
    { value: "לילה ללא תאורה", en: "Night without lighting", he: "לילה ללא תאורה" }
  ],
  SUG_DEREH: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "עירוני בצומת", en: "Urban at Junction", he: "עירוני בצומת" },
    { value: "עירוני לא בצומת", en: "Urban not at Junction", he: "עירוני לא בצומת" },
    { value: "לא עירוני בצומת", en: "Non-urban at Junction", he: "לא עירוני בצומת" },
    { value: "לא עירוני לא בצומת", en: "Non-urban not at Junction", he: "לא עירוני לא בצומת" }
  ],
  PNE_KVISH: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "יבש", en: "Dry", he: "יבש" },
    { value: "רטוב ממים", en: "Wet", he: "רטוב ממים" },
    { value: "מרוח בחומר דלק", en: "Fuel on Surface", he: "מרוח בחומר דלק" },
    { value: "מכוסה בבוץ", en: "Mud", he: "מכוסה בבוץ" }
  ],
  TKINUT: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "תקין", en: "Valid", he: "תקין" },
    { value: "לא תקין", en: "Invalid", he: "לא תקין" }
  ],
  MEZEG_AVIR: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "בהיר", en: "Clear", he: "בהיר" },
    { value: "מעונן", en: "Cloudy", he: "מעונן" },
    { value: "גשום", en: "Rainy", he: "גשום" },
    { value: "ערפילי", en: "Foggy", he: "ערפילי" }
  ],
  YOM_LAYLA: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "יום", en: "Day", he: "יום" },
    { value: "לילה", en: "Night", he: "לילה" }
  ],
  SUG_TEUNA: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "חזיתי", en: "Frontal", he: "חזיתי" },
    { value: "אחורי", en: "Rear-end", he: "אחורי" },
    { value: "צדדי", en: "Side", he: "צדדי" },
    { value: "הולך רגל", en: "Pedestrian", he: "הולך רגל" }
  ],
  SIMUN_TIMRUR: [
    { value: "לא ידוע", en: "Unknown", he: "לא ידוע" },
    { value: "בעל רמזור", en: "Traffic Light", he: "בעל רמזור" },
    { value: "בעל תמרור", en: "Traffic Sign", he: "בעל תמרור" },
    { value: "ללא סימונים", en: "No Marking", he: "ללא סימונים" }
  ]
};

let lastBreakdownData = [];
let lastProbability = null;

function getCurrentLanguage() {
  return document.documentElement.lang === "he" ? "he" : "en";
}

function getApiEndpoint() {
  const currentPort = window.location.port;
  const currentHost = window.location.hostname;
  if (currentPort === "8000") {
    return "/predict";
  }
  return `http://${currentHost}:8001/predict`;
}

function applyI18nText(lang) {
  document.querySelectorAll("[data-i18n]").forEach((element) => {
    const key = element.getAttribute("data-i18n");
    if (i18n[lang][key]) {
      element.textContent = i18n[lang][key];
    }
  });
}

function renderOptionsForSelect(selectId, lang) {
  const select = document.getElementById(selectId);
  const options = selectOptions[selectId];
  if (!select || !options) {
    return;
  }

  const currentValue = select.value;
  select.innerHTML = "";

  options.forEach((item) => {
    const option = document.createElement("option");
    option.value = item.value;
    const englishText = String(item.en ?? "").split("/")[0].trim();
    const hebrewText = String(item.he ?? "").split("/").pop().trim();
    option.textContent = lang === "he" ? (hebrewText || englishText) : (englishText || hebrewText);
    select.appendChild(option);
  });

  const hasPrevious = options.some((item) => item.value === currentValue);
  if (hasPrevious) {
    select.value = currentValue;
  } else if (selectId === "HODESH_TEUNA") {
    select.value = String(new Date().getMonth() + 1);
  } else if (selectId === "SHAA_HOUR") {
    select.value = String(new Date().getHours());
  } else if (selectId === "SHAA_MINUTE") {
    const currentMinute = new Date().getMinutes();
    const roundedMinute = String(Math.floor(currentMinute / 15) * 15).padStart(2, "0");
    select.value = roundedMinute;
  }
}

function renderAllSelectOptions(lang) {
  Object.keys(selectOptions).forEach((selectId) => renderOptionsForSelect(selectId, lang));
  updateSelectVisualState();
}

function updateSelectVisualState() {
  document.querySelectorAll(".input-group select").forEach((select) => {
    const hasValue = String(select.value || "").trim() !== "";
    select.classList.toggle("is-selected", hasValue);
  });
}

function classifyRisk(probability) {
  const lang = getCurrentLanguage();
  if (probability < 0.33) {
    return { label: i18n[lang].low_risk_label, badge: i18n[lang].low, cssClass: "risk-low", color: "#2e7d32" };
  }
  if (probability < 0.66) {
    return { label: i18n[lang].medium_risk_label, badge: i18n[lang].medium, cssClass: "risk-medium", color: "#ed6c02" };
  }
  return { label: i18n[lang].high_risk_label, badge: i18n[lang].high, cssClass: "risk-high", color: "#d32f2f" };
}

function setAdvice(probability) {
  const lang = getCurrentLanguage();
  if (probability < 0.33) {
    return i18n[lang].low_risk_advice;
  }
  if (probability < 0.66) {
    return i18n[lang].medium_risk_advice;
  }
  return i18n[lang].high_risk_advice;
}

function renderBreakdown(breakdown) {
  const explainDiv = document.getElementById("explain");
  if (!explainDiv) {
    return;
  }

  const lang = getCurrentLanguage();
  explainDiv.innerHTML = `<div class="risk-factors-title">${i18n[lang].why_this_risk}</div>`;

  if (!Array.isArray(breakdown) || breakdown.length === 0) {
    return;
  }

  const list = document.createElement("div");
  list.className = "risk-factors-list";

  breakdown.forEach((item) => {
    if (!item || typeof item !== "object") {
      return;
    }

    const factor = String(item.factor ?? "");
    const value = String(item.value ?? "");
    const delta = Number(item.delta ?? 0);
    const impact = Math.round(delta * 100);

    const factorLabel = i18n[lang][`factor_${factor}`] || factor;
    const signedImpact = impact >= 0 ? `+${impact}%` : `${impact}%`;

    const factorItem = document.createElement("div");
    factorItem.className = "risk-factor-item";
    factorItem.innerHTML = `
      <div class="factor-label">${factorLabel}</div>
      <div class="factor-value">${value}</div>
      <div class="factor-impact ${impact >= 0 ? "positive" : "negative"}">${signedImpact}</div>
    `;

    list.appendChild(factorItem);
  });

  explainDiv.appendChild(list);
}

function applyRiskTheme(probability) {
  const resultSection = document.querySelector(".result-section");
  const explainDiv = document.getElementById("explain");
  if (!resultSection || !explainDiv) {
    return;
  }

  resultSection.classList.remove("risk-theme-low", "risk-theme-medium", "risk-theme-high");
  explainDiv.classList.remove("risk-factors--low", "risk-factors--medium", "risk-factors--high");

  if (probability < 0.33) {
    resultSection.classList.add("risk-theme-low");
    explainDiv.classList.add("risk-factors--low");
    return;
  }

  if (probability < 0.66) {
    resultSection.classList.add("risk-theme-medium");
    explainDiv.classList.add("risk-factors--medium");
    return;
  }

  resultSection.classList.add("risk-theme-high");
  explainDiv.classList.add("risk-factors--high");
}

function setLanguage(lang) {
  if (!i18n[lang]) {
    return;
  }

  document.documentElement.lang = lang;
  document.documentElement.dir = lang === "he" ? "rtl" : "ltr";
  applyI18nText(lang);
  renderAllSelectOptions(lang);

  document.querySelectorAll(".lang-btn").forEach((btn) => {
    btn.classList.toggle("active", btn.getAttribute("data-lang") === lang);
  });

  const advice = document.getElementById("advice");
  if (advice) {
    advice.textContent = lastProbability === null ? i18n[lang].select_conditions_advice : setAdvice(lastProbability);
  }

  if (lastBreakdownData.length > 0) {
    renderBreakdown(lastBreakdownData);
  }

  if (lastProbability !== null) {
    const cls = classifyRisk(lastProbability);
    const percent = Math.round(lastProbability * 100);
    const riskText = document.getElementById("riskText");
    const riskBadge = document.getElementById("riskBadge");
    if (riskText) {
      riskText.textContent = `${percent}% (${cls.label})`;
      riskText.style.color = cls.color;
    }
    if (riskBadge) {
      riskBadge.textContent = cls.badge;
      riskBadge.className = `risk-badge ${cls.cssClass}`;
    }
  }

  localStorage.setItem("ui_language", lang);
}

function initializeLanguage() {
  const saved = localStorage.getItem("ui_language");
  setLanguage(saved === "he" ? "he" : "en");
}

function getNumericValue(id, fallback) {
  const node = document.getElementById(id);
  if (!node) {
    return fallback;
  }
  const value = Number(node.value);
  return Number.isFinite(value) ? value : fallback;
}

function getStringValue(id, fallback) {
  const node = document.getElementById(id);
  if (!node) {
    return fallback;
  }
  const value = String(node.value || "").trim();
  return value === "" ? fallback : value;
}

function getTimeValue(fallback) {
  const hour = getStringValue("SHAA_HOUR", "");
  const minute = getStringValue("SHAA_MINUTE", "");
  if (!hour || !minute) {
    return fallback;
  }
  return `${hour.padStart(2, "0")}:${minute.padStart(2, "0")}`;
}

function getFieldLabel(id, lang) {
  if (id === "SHAA_HOUR") {
    return lang === "he" ? "שעה" : "Hour";
  }
  if (id === "SHAA_MINUTE") {
    return lang === "he" ? "דקות" : "Minutes";
  }
  const labelNode = document.querySelector(`label[for="${id}"]`);
  if (labelNode && labelNode.textContent.trim()) {
    return labelNode.textContent.trim();
  }
  return i18n[lang][`label_${id}`] || id;
}

function validateRequiredFields() {
  const lang = getCurrentLanguage();
  const missingFields = [];

  Object.keys(selectOptions).forEach((id) => {
    const node = document.getElementById(id);
    if (!node || String(node.value || "").trim() === "") {
      missingFields.push(getFieldLabel(id, lang));
    }
  });

  if (missingFields.length === 0) {
    return { valid: true, message: "" };
  }

  return {
    valid: false,
    message: i18n[lang].validation_required_message.replace("{fields}", missingFields.join(", "))
  };
}

function showValidationError(message) {
  const lang = getCurrentLanguage();
  const errorText = document.getElementById("errorText");
  const errorTitle = errorText ? errorText.querySelector("h3") : null;
  const errorBody = errorText ? errorText.querySelector("p") : null;
  const advice = document.getElementById("advice");

  if (errorText) {
    errorText.style.display = "block";
  }
  if (errorTitle) {
    errorTitle.textContent = i18n[lang].validation_required_title;
  }
  if (errorBody) {
    errorBody.textContent = message;
  }
  if (advice) {
    advice.textContent = message;
  }
}

async function predict() {
  const lang = getCurrentLanguage();
  const btn = document.getElementById("btn");
  const btnText = document.querySelector(".btn-text");
  const btnLoading = document.querySelector(".btn-loading");
  const riskText = document.getElementById("riskText");
  const riskBadge = document.getElementById("riskBadge");
  const advice = document.getElementById("advice");
  const explainDiv = document.getElementById("explain");
  const errorText = document.getElementById("errorText");
  const gaugeNeedle = document.getElementById("gaugeNeedle");
  const lightProb = document.getElementById("lightProb");
  const dangerousProb = document.getElementById("dangerousProb");

  if (!btn || !btnText || !btnLoading || !riskText || !riskBadge || !advice || !explainDiv || !errorText || !gaugeNeedle || !lightProb || !dangerousProb) {
    return;
  }

  errorText.style.display = "none";
  btn.disabled = true;
  btnText.style.display = "none";
  btnLoading.style.display = "inline";

  const validation = validateRequiredFields();
  if (!validation.valid) {
    showValidationError(validation.message);
    btn.disabled = false;
    btnText.style.display = "inline";
    btnLoading.style.display = "none";
    return;
  }

  riskText.textContent = "...";
  riskText.style.color = "";
  riskBadge.textContent = i18n[lang].ready;
  riskBadge.className = "risk-badge";
  advice.textContent = i18n[lang].calculating;
  explainDiv.textContent = "";

  const payload = {
    SHAA: getTimeValue("00:00"),
    HODESH_TEUNA: getStringValue("HODESH_TEUNA", "1"),
    YOM_BASHAVUA: getStringValue("YOM_BASHAVUA", "לא ידוע"),
    SUG_TEUNA: getStringValue("SUG_TEUNA", "לא ידוע"),
    ROAD_STRUCTURE: getStringValue("ROAD_STRUCTURE", "לא ידוע"),
    ROHAV: getStringValue("ROHAV", "לא ידוע"),
    NAFA: getStringValue("NAFA", "לא ידוע"),
    ZURAT_ISHUV: getStringValue("ZURAT_ISHUV", "לא ידוע"),
    MEHIRUT_MUTERET: getStringValue("MEHIRUT_MUTERET", "לא ידוע"),
    TEURA: getStringValue("TEURA", "לא ידוע"),
    SUG_DEREH: getStringValue("SUG_DEREH", "לא ידוע"),
    SIMUN_TIMRUR: getStringValue("SIMUN_TIMRUR", "לא ידוע"),
    TKINUT: getStringValue("TKINUT", "לא ידוע"),
    PNE_KVISH: getStringValue("PNE_KVISH", "לא ידוע"),
    MEZEG_AVIR: getStringValue("MEZEG_AVIR", "לא ידוע"),
    YOM_LAYLA: getStringValue("YOM_LAYLA", "לא ידוע")
  };

  try {
    const response = await fetch(getApiEndpoint(), {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const data = await response.json();
    const probability = Number(data.probability);
    if (!Number.isFinite(probability) || probability < 0 || probability > 1) {
      throw new Error("invalid_probability");
    }

    const percent = Number.isFinite(Number(data.risk_percent)) ? Number(data.risk_percent) : Math.round(probability * 100);
    const cls = classifyRisk(probability);

    lastProbability = probability;
    lastBreakdownData = Array.isArray(data.breakdown) ? data.breakdown : [];

    riskText.textContent = `${percent}% (${cls.label})`;
    riskText.style.color = cls.color;
    riskBadge.textContent = cls.badge;
    riskBadge.className = `risk-badge ${cls.cssClass}`;
    advice.textContent = setAdvice(probability);

    gaugeNeedle.style.left = `${Math.max(0, Math.min(100, percent))}%`;
    dangerousProb.textContent = `${Math.max(0, Math.min(100, percent))}%`;
    lightProb.textContent = `${Math.max(0, 100 - Math.max(0, Math.min(100, percent)))}%`;

    renderBreakdown(lastBreakdownData);
    applyRiskTheme(probability);
  } catch (error) {
    let userMessage = i18n[lang].server_error;
    if (error instanceof TypeError) {
      userMessage = i18n[lang].network_error;
    } else if (String(error.message).includes("invalid_probability")) {
      userMessage = i18n[lang].invalid_response;
    }

    errorText.style.display = "block";
    advice.textContent = userMessage;
    riskBadge.textContent = i18n[lang].error;
    riskBadge.className = "risk-badge risk-error";
  } finally {
    btn.disabled = false;
    btnText.style.display = "inline";
    btnLoading.style.display = "none";
  }
}

function bindEvents() {
  document.querySelectorAll(".lang-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const lang = btn.getAttribute("data-lang") === "he" ? "he" : "en";
      setLanguage(lang);
    });
  });

  const predictButton = document.getElementById("btn");
  if (predictButton) {
    predictButton.addEventListener("click", (event) => {
      event.preventDefault();
      predict();
    });
  }

  document.querySelectorAll(".input-group select").forEach((select) => {
    select.addEventListener("change", updateSelectVisualState);
  });
}

function initializeApp() {
  initializeLanguage();
  renderAllSelectOptions(getCurrentLanguage());
  bindEvents();

  document.querySelectorAll(".input-group select").forEach((select) => {
    select.required = true;
    select.setAttribute("aria-required", "true");
  });

  const advice = document.getElementById("advice");
  if (advice) {
    advice.textContent = i18n[getCurrentLanguage()].select_conditions_advice;
  }

  const gaugeNeedle = document.getElementById("gaugeNeedle");
  if (gaugeNeedle) {
    gaugeNeedle.style.left = "0%";
  }

  const lightProb = document.getElementById("lightProb");
  const dangerousProb = document.getElementById("dangerousProb");
  if (lightProb) {
    lightProb.textContent = "--%";
  }
  if (dangerousProb) {
    dangerousProb.textContent = "--%";
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initializeApp);
} else {
  initializeApp();
}
