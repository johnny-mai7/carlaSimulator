#ifndef XMLFILES_HPP
#define XMLFILES_HPP

#include "File.hpp"
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>

struct MagazineData
{
    std::string name;
    std::vector<std::string> content;
};

class XMLFiles : public File
{
public:
    XMLFiles();
    XMLFiles(const std::string &filename);

    virtual void open() override;
    virtual void load() override;
    virtual void close() override;

protected:
    MagazineData magazine_data;
    void parse_data();
};

#endif
