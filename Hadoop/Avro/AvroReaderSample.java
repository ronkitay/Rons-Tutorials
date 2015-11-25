package com.akamai.reputation.jobs.heuristics.samples;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.ByteBuffer;

import org.apache.avro.file.DataFileReader;
import org.apache.avro.file.FileReader;
import org.apache.avro.file.SeekableInput;
import org.apache.avro.generic.GenericDatumReader;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.io.DatumReader;
import org.apache.avro.mapred.FsInput;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.LocatedFileStatus;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.RemoteIterator;
import org.junit.Ignore;
import org.junit.Test;

import static com.akamai.csi.commons.string.StringUtils.b2s;

public class TestAvroOutput {

	public static void main(String[] args) throws IOException {
		printAvroFile(new Configuration(), new Path("/Users/rkitay/tmp/h36/WAF_DLR-10.24.162.9_189514_1433365956259_6426-2.avro.deflate"));
	}

	public static void printAvroFile(Configuration config, Path path) throws IOException{
		BufferedWriter br = new BufferedWriter(new FileWriter("/Users/rkitay/tmp/h36/chunk.json"));
		SeekableInput input = new FsInput(path, config);
		input.seek(536870912); // Go to block's start
		DatumReader<GenericRecord> reader = new GenericDatumReader<GenericRecord>();
		FileReader<GenericRecord> fileReader = DataFileReader.openReader(input, reader);

		for (GenericRecord datum : fileReader) {
			if (input.tell()>134217728) { // Check the block (128MB) did not end
				break;
			}
			final ByteBuffer query = (ByteBuffer) datum.get("query");
			br.append(b2s(query.array()));
			br.newLine();
		}

		fileReader.close(); // also closes underlying FsInput
		br.close();
	}
	
	@Ignore
	@Test
	public void testAvroOutput() throws IOException{
		Path basePath = new Path("/Users/olevin/work/akamai/csi2/csi-jobs/csi-reputation-jobs/reputation-jobs-flow/target/akamai/csi/work/reputation/etl/evidence_raw_data/");
		Configuration config = new Configuration(); // make this your Hadoop env config
		FileSystem fs = FileSystem.get(config);
		
		RemoteIterator<LocatedFileStatus> it = fs.listFiles(basePath, true);
		
		while(it.hasNext()){
			FileStatus f = it.next();
			if(f.isFile()){
				printAvroFile(config, f.getPath());
			}
		}
	}
}
