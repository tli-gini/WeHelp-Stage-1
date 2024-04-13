// Task 1
// We just received messages from 5 friends in JSON format, and we want to take the green
// line, including Xiaobitan station, of Taipei MRT to meet one of them. Write code to find out
// the nearest friend and print name, based on any given station currently located at and
// station count between two stations.
console.log("===== Task 1 =====");

function findAndPrint(messages, currentStation) {
  const stationsOrder = [
    [
      "Songshan",
      "Nanjing Sanmin",
      "Taipei Arena",
      "Nanjing Fuxing",
      "Songjiang Nanjing",
      "Zhongshan",
      "Beimen",
      "Ximen",
      "Xiaonanmen",
      "Chiang Kai-Shek Memorial Hall",
      "Guting",
      "Taipower Building",
      "Gongguan",
      "Wanlong",
      "Jingmei",
      "Dapinglin",
      "Qizhang",
      "Xindian City Hall",
      "Xindian",
    ],
    [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "Xiaobitan",
      "",
      "",
    ],
  ];

  const findStationPosition = (stationName) => {
    for (let y = 0; y < stationsOrder.length; y++) {
      const line = stationsOrder[y];
      for (let x = 0; x < line.length; x++) {
        if (line[x] === stationName) {
          return { x, y };
        }
      }
    }
    return { x: -1, y: -1 };
  };

  const currentStationIndex = findStationPosition(currentStation);

  let closestFriend = "";
  let closestDistance = Infinity;

  Object.entries(messages).forEach(([name, message]) => {
    stationsOrder.flat().forEach((station) => {
      if (message.includes(station) && station) {
        const friendIndex = findStationPosition(station);
        const distance =
          Math.abs(currentStationIndex.x - friendIndex.x) +
          Math.abs(currentStationIndex.y - friendIndex.y);

        if (distance < closestDistance) {
          closestDistance = distance;
          closestFriend = name;
        }
      }
    });
  });

  console.log(closestFriend);
}

const messages = {
  Bob: "I'm at Ximen MRT station.",
  Mary: "I have a drink near Jingmei MRT station.",
  Copper: "I just saw a concert at Taipei Arena.",
  Leslie: "I'm at home near Xiaobitan station.",
  Vivian: "I'm at Xindian station waiting for you.",
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian

// Task 2
// Assume we have consultants for consulting services. Help people book the best matching
// consultant in a day, based on hours, service durations, and selection criteria.
// 1. Booking requests are one by one, order matters.
// 2. A consultant is only available if there is no overlapping between already booked time
//    and an incoming request time.
// 3. If the criteria is "price", choose the available consultant with the lowest price.
// 4. If the criteria is "rate", choose the available consultant with the highest rate.
// 5. If every consultant is unavailable, print "No Service".
console.log("===== Task 2 =====");

function book(consultants, hour, duration, criteria) {
  if (!this.schedule) {
    this.schedule = {};
  }

  let availableConsultants = [];
  for (let i = 0; i < consultants.length; i++) {
    let available = true;
    for (let j = hour; j < hour + duration; j++) {
      if (
        this.schedule[consultants[i].name] &&
        this.schedule[consultants[i].name][j]
      ) {
        available = false;
      }
    }
    if (available) {
      availableConsultants.push(consultants[i]);
    }
  }

  if (criteria === "price") {
    availableConsultants.sort((a, b) => a.price - b.price);
  } else if (criteria === "rate") {
    availableConsultants.sort((a, b) => b.rate - a.rate);
  }
  if (availableConsultants.length === 0) {
    console.log("No Service");
    return;
  }

  const yourConsultant = availableConsultants[0];
  if (!this.schedule[yourConsultant.name]) {
    this.schedule[yourConsultant.name] = {};
  }
  for (let i = hour; i < hour + duration; i++) {
    this.schedule[yourConsultant.name][i] = true;
  }
  console.log(yourConsultant.name);
}

const consultants = [
  { name: "John", rate: 4.5, price: 1000 },
  { name: "Bob", rate: 3, price: 1200 },
  { name: "Jenny", rate: 3.8, price: 800 },
];

book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John

// Task 3
// Find out whose middle name is unique among all the names, and print it. You can assume
// every input is a Chinese name with 2 ~ 5 words. If there are only 2 words in a name, the
// middle name is defined as the second word. If there are 4 words in a name, the middle name
// is defined as the third word.
console.log("===== Task 3 =====");

function func(...data) {
  // your code here
  const wordsList = {};

  data.forEach((str, index) => {
    let middleName;
    if (str.length === 2 || str.length === 3) {
      middleName = str.charAt(1);
    } else if (str.length === 4 || str.length === 5) {
      middleName = str.charAt(2);
    }

    if (!wordsList[middleName]) {
      wordsList[middleName] = [];
    }

    wordsList[middleName].push(index);
  });

  const uniqueIndex = [];
  for (let word in wordsList) {
    if (wordsList[word].length === 1) {
      uniqueIndex.push(wordsList[word][0]);
    }
  }

  if (uniqueIndex.length === 0) {
    console.log("沒有");
  } else {
    for (let i = 0; i < uniqueIndex.length; i++) {
      console.log(data[uniqueIndex[i]]);
    }
  }
}

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安

// Task 4
// There is a number sequence: 0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25, …
// Find out the nth term in this sequence.
// +4,+4,-1

console.log("===== Task 4 =====");

function getNumber(index) {
  let a = 0;
  for (let i = 1; i <= index; i++) {
    if (i % 3 === 0) {
      a -= 1;
    } else {
      a += 4;
    }
  }
  console.log(a);
}
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70
