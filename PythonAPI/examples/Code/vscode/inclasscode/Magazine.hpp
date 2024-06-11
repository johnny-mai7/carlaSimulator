#ifndef MAGAZINE_HPP
#define MAGAZINE_HPP

#include "XMLFiles.hpp"

class Magazine : public XMLFiles
{
public:
    Magazine();
    Magazine(const std::string &filename);

    virtual void open() override;
    virtual void load() override;
    virtual void close() override;

    void write_data(const std::string &output_filename);
    std::string to_string();

private:
    std::string format_data();
};

#endif
