# AI Document Summariser Tool
# This tool takes any text and uses Groq AI to generate a summary and key insights

from groq import Groq

# Setting up the Groq client with API key
# Get your free API key at console.groq.com
api_key = "your_groq_api_key_here"
client = Groq(api_key=api_key)


def summarise_text(text):
    # Sending the text to Groq API and asking it to summarise
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""Please analyse the following text and provide:
                1. A concise summary (3-4 sentences)
                2. Five key points
                3. Main topics covered

                Text to analyse:
                {text}"""
            }
        ]
    )
    return response.choices[0].message.content

def main():
    print("=" * 50)
    print("   AI Document Summariser Tool")
    print("=" * 50)
    print("\nPaste your text below and press Enter twice when done:\n")
    
    # Collecting multi-line input from user
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    text = "\n".join(lines)
    
    if not text:
        print("Come on man, text something.")
        return
    
    print("\n Yo Wait for me...\n")
    
    # Getting the summary from Groq
    result = summarise_text(text)
    
    print("=" * 50)
    print("   ANALYSIS RESULTS")
    print("=" * 50)
    print(result)

# Running the main function
if __name__ == "__main__":
    main()