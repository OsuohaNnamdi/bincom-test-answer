import re
from collections import Counter
import statistics
from typing import List

class BincomColorAnalyzer:
    def __init__(self):
        self.html_content = """
        <html>
        <head>
        <title>Our Python Class exam</title>
        </head>
        <body>
        <h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
        <table>
            
            <thead>
                <th>DAY</th><th>COLOURS</th>
            </thead>
            <tbody>
            <tr>
                <td>MONDAY</td>
                <td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
            </tr>
            <tr>
                <td>TUESDAY</td>
                <td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
            </tr>
            <tr>
                <td>WEDNESDAY</td>
                <td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
            </tr>
            <tr>
                <td>THURSDAY</td>
                <td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
            </tr>
            <tr>
                <td>FRIDAY</td>
                <td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
            </tr>
            </tbody>
        </table>
        </body>
        </html>
        """
        self.all_colors = self.extract_colors()
        self.color_frequencies = Counter(self.all_colors)
    
    def extract_colors(self) -> List[str]:
        pattern = r'<td>[A-Z]+, [A-Z]+.*?</td>'
        color_rows = re.findall(pattern, self.html_content)
        
        all_colors = []
        for row in color_rows:
            colors_text = re.search(r'<td>([A-Z].*?)</td>', row).group(1)
            colors = [color.strip().upper() for color in colors_text.split(',')]
            all_colors.extend(colors)
        
        return all_colors
    
    def get_mean_color(self) -> str:
        return self.color_frequencies.most_common(1)[0][0]
    
    def get_most_worn_color(self) -> str:
        return self.color_frequencies.most_common(1)[0][0]
    
    def get_median_color(self) -> str:
        sorted_colors = sorted(self.color_frequencies.items(), 
                             key=lambda x: x[1], reverse=True)
        median_index = len(sorted_colors) // 2
        return sorted_colors[median_index][0]
    
    def get_color_variance(self) -> float:
        frequencies = list(self.color_frequencies.values())
        return statistics.variance(frequencies) if len(frequencies) > 1 else 0
    
    def get_red_probability(self) -> float:
        total_colors = len(self.all_colors)
        red_count = self.color_frequencies.get('RED', 0)
        return red_count / total_colors if total_colors > 0 else 0