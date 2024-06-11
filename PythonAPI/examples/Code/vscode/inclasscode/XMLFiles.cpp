#include "XMLFiles.hpp"

XMLFiles::XMLFiles() : File() {}

XMLFiles::XMLFiles(const std::string &filename) : File(filename) {}

void XMLFiles::open()
{
    // Open file and validate it here
}

void XMLFiles::load()
{
    // Load the file to a structure
}

void XMLFiles::close()
{
    // Close the file
}

void XMLFiles::parse_data()
{
    // Parse data between the tags
}
